
import ssl
from httpx import AsyncClient
from bs4 import BeautifulSoup as BS
from random import choice
from urllib.parse import urljoin


from APP.config import base_urls, headers, timeout
from APP.utils.make_async import make_async
from APP.models.post import Post


async def index_posts(board_url, category, subject, requests_semaphore, profile):
    async with requests_semaphore:
        async with AsyncClient() as client:
            tried_urls = []
            r = True
            while r:
                try:
                    possible_urls = [url for url in base_urls if url not in tried_urls]
                    used_url = choice(possible_urls)
                    tried_urls.append(used_url)
                    board_url = urljoin(used_url, board_url)
                    response = await client.get(board_url, headers=headers, timeout=timeout, follow_redirects=True)
                    r = False
                except ssl.SSLError:
                    print(f'SSL Error with {used_url} Retrying...')
                    pass

                except Exception as e:
                    raise e
                if not response.status_code == 200:
                    print(f'Error with {used_url}, status code {response.status_code}')
                    r = False
                    continue
                try:
                    soup = BS(response.content, 'lxml')
                    posts_container = soup.find(class_="opCell")
                    origin_post = posts_container.find(class_="innerOP")
                    media_replies = [p for p in posts_container.find_all(class_="postCell") if p.find_all(class_="panelUploads")]
                    media_posts = media_replies + [origin_post] if origin_post.find_all(class_="panelUploads") else media_replies
                    async for post in make_async(media_posts):
                        message = post.find(class_="divMessage").text
                        author = post.find(class_="linkName").text
                        post_id = post.find(class_="deletionCheckBox")['name']
                        post_category = category
                        post_subject = subject
                        post_media = [x['href'] for x in post.find_all(class_="nameLink")]
                        px = Post(post_id, message, author, category, subject, post_media)
                        px.save(profile)
                except Exception as e:
                    raise e

