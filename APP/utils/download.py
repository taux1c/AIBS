import aiofiles
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pathlib import Path
from random import choice
from urllib.parse import urljoin
from tqdm import tqdm
from asyncio import Semaphore, Queue, get_running_loop
from httpx import AsyncClient

from APP.utils.profiles import select_profile
from APP.models.post import Post
from APP.utils.sanitize_path import sanitize_name
from APP.config import headers, timeout, base_urls

loop = get_running_loop()
download_queue = Queue(loop=loop)

async def download_start():
    profile = select_profile()
    requests_semaphore = Semaphore(profile.max_concurrent_requests)
    async with requests_semaphore:
        async with AsyncClient() as client:
            engine = create_engine(profile.db_string)
            Session = sessionmaker(bind=engine)
            with Session() as session:
                results = session.query(Post).filter(Post.downloaded == False)
                if results is not None:
                    for result in results:
                        for media in result.media:
                            save_location = Path(profile.save_location, result.category, sanitize_name(result.subject), sanitize_name(result.message), sanitize_name(result.author))
                            save_location.mkdir(parents=True, exist_ok=True)
                            await download_queue.put(final_download(save_location=save_location, media=media, profile=profile, client=client))

async def download():
    for i in range(10):
        loop.create_task(download_worker())
        await download_start()

async def final_download(save_location=None, media=None, profile=None, client=None):
    file_name = media.split('/')[-1]
    tried_urls = []
    possible_urls = [x for x in base_urls if x not in tried_urls]
    used_url = choice(possible_urls)
    async with client.stream("GET", media, headers=headers, timeout=timeout) as response:
        async with aiofiles.open(Path(save_location, file_name), mode='wb') as f:
            async for chunk in response.aiter_bytes():
                await f.write(chunk)

async def download_worker():
    while download_queue.qsize() > 0:
        task = download_queue.get()
        await task