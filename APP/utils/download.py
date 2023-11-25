

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pathlib import Path
from asyncio import sleep
from httpx import AsyncClient
from urllib.parse import urljoin
from random import choice
from json import loads



from APP.models.post import Post
from APP.config import headers, timeout, base_urls
from APP.utils.profiles import select_profile
from APP.utils.sanitize_path import sanitize_name





# This eventually needs to be changed to an async session to open event loop back up.
async def download():
    global x
    profile = select_profile()
    engine = create_engine(profile.db_string, pool_pre_ping=True)
    with engine.begin() as con:
        Session = sessionmaker(bind=con)
        with Session() as session:
            results = session.query(Post).filter(Post.downloaded == False).all()

            for result in results:
                    for url in loads(result.media):
                        filename = url.split('/')[-1]
                        save_location = Path(profile.save_location)
                        save_location.mkdir(parents=True, exist_ok=True)
                        fp = Path(save_location, result.category, sanitize_name(result.subject), sanitize_name(result.message), sanitize_name(result.author))
                        fp.mkdir(parents=True, exist_ok=True)
                        file_obj = Path(fp, filename[-15:])
                        async with AsyncClient(follow_redirects=True) as browser_session:
                            x = True
                            tried_urls = []
                            while x:
                                try:
                                    possible_urls = [url for url in base_urls if url not in tried_urls]
                                    if len(possible_urls) == 0:
                                        x = False
                                        continue
                                    else:
                                        used_url = choice(possible_urls)
                                        tried_urls.append(used_url)
                                    url = urljoin(used_url, url)
                                    response = await browser_session.get(url, headers=headers, timeout=timeout)
                                    print(f"Downloading {file_obj}.")
                                    with open(file_obj, 'wb') as f:
                                        f.write(response.content)


                                    # Create a second session specifically for updating the downloaded status
                                    with engine.begin() as con2:
                                        session2 = Session(bind=con2)
                                        post_to_update = session2.query(Post).filter_by(id=result.id).first()
                                        post_to_update.downloaded = True
                                        session2.commit()
                                    x = False

                                except Exception as e:
                                    # Handle exceptions or log error messages
                                    print(f"Error processing Post {result.id}: {e}")
                                    pass
    # Commit any remaining changes and close the session
    session.commit()
    session.close()



