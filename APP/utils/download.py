from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from httpx import AsyncClient
import aiofiles
from pathlib import Path
from random import choice
from urllib.parse import urljoin
from tqdm import tqdm
from asyncio import get_running_loop, as_completed, gather, get_event_loop

from APP.utils.profiles import select_profile
from APP.models.post import Post
from APP.utils.make_async import make_async, async_as_completed
from APP.config import headers, timeout, base_urls
from APP.utils.sanitize_path import sanitize_name


async def download(profile=None):
    if profile is None:
        profile = select_profile()
    loop = get_running_loop()
    engine = create_engine(profile.db_string)
    Session = sessionmaker(bind=engine)
    try:
        async with AsyncClient() as client:
            download_tasks = []
            with Session() as session:
                results = session.query(Post).filter(Post.downloaded == False).all()
                for result in results:
                    download_tasks.append(loop.create_task(final_download(result.post_id, profile, client)))

                pbar = tqdm(total=len(download_tasks), desc="Downloading", unit="files")
                async for task in async_as_completed(download_tasks):
                    pbar.update(1)
                pbar.close()
    except Exception as e:
        print(e)
    finally:
        engine.dispose()

async def final_download(result, profile, client):
    e = create_engine(profile.db_string)
    S = sessionmaker(bind=e)
    with S() as s:
        result = s.query(Post).filter(Post.post_id == result).first()
        result.load()
        async for item in make_async(result.media):
            save_location = Path(await sanitize_name(str(profile.save_location)), await sanitize_name(result.category), await sanitize_name(result.subject), await sanitize_name(result.message), await sanitize_name(result.author))
            save_location.mkdir(parents=True, exist_ok=True)
            tried_urls = []
            file_name = item.split('/')[-1]
            file_path = Path(save_location, file_name)
            while True:
                try:
                    possible_urls = [u for u in base_urls if u not in tried_urls]
                    used_url = choice(possible_urls)
                    tried_urls.append(used_url)
                    url = urljoin(used_url, item)
                    async with client.stream('GET', url, headers=headers, timeout=timeout) as r:
                        async with aiofiles.open(file_path, 'wb') as f:
                            async for chunk in r.aiter_bytes():
                                await f.write(chunk)

                    result.downloaded = True
                    result.dump()
                    s.commit()
                    break
                except Exception as e:
                    while len(tried_urls) < len(base_urls):
                        pass
                    else:
                        break