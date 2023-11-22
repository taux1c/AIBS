
import ssl
from httpx import AsyncClient
from bs4 import BeautifulSoup
from random import choice
from urllib.parse import urljoin


from config import base_urls
from config import headers, timeout

# Pick a random base url to use to avoid hitting the same url over and over. (All urls hit the same server but cloudflare
# will block you if you hit the same url too many times in a row.) Adding proxies soon.
base_url = choice(base_urls)


async def find_boards(board:str, requests_semaphore):
    async with requests_semaphore:
        async with AsyncClient() as client:
            tried_urls = []
            r = True
            while r:
                try:
                    possible_urls = [url for url in base_urls if url not in tried_urls]
                    used_url = choice(possible_urls)
                    tried_urls.append(used_url)
                    board_url = urljoin(used_url, board)
                    response = await client.get(urljoin(base_url, board), headers=headers, timeout=timeout, follow_redirects=True)
                    soup = BeautifulSoup(response.content, 'html.parser')
                    boards = soup.find_all(class_="opCell")
                    return boards
                except ssl.SSLError:
                    pass

                except Exception as e:
                    r = False
                    raise e