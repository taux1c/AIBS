
import ssl
from httpx import AsyncClient, TimeoutException, HTTPError
from bs4 import BeautifulSoup
from random import choice
from urllib.parse import urljoin
from asyncio import sleep


from APP.config import base_urls
from APP.config import headers, timeout

# Pick a random base url to use to avoid hitting the same url over and over. (All urls hit the same server but cloudflare
# will block you if you hit the same url too many times in a row.) Adding proxies soon.
base_url = choice(base_urls)


async def find_boards(board:str, requests_semaphore):
    async with requests_semaphore:
        async with AsyncClient() as client:
            tried_urls = []
            r = True
            attempt = 0
            while r:
                try:
                    possible_urls = [url for url in base_urls if url not in tried_urls]
                    if len(possible_urls) == 0:
                        r = False
                        continue
                    used_url = choice(possible_urls)
                    tried_urls.append(used_url)
                    board_url = urljoin(used_url, board)
                    response = await client.get(board_url, headers=headers, timeout=timeout, follow_redirects=True)
                    if not response:
                        r = False
                        continue
                    if response is None or response.status_code != 200:
                        print(f'Error with {used_url}, status code {response.status_code}')
                        r = False
                    soup = BeautifulSoup(response.content, 'html.parser')
                    boards = soup.find_all(class_="opCell")
                    return boards
                except ssl.SSLError:
                    pass
                except (TimeoutException, HTTPError) as exc:
                    print(f"Attempt {attempt + 1} failed: {exc}")
                    await sleep(1)

                except Exception as e:
                    r = False
                    raise e