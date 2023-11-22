
from asyncio import Semaphore
from tqdm import tqdm



from APP.utils.make_async import make_async
from APP.scrapers.find_boards import find_boards
from APP.scrapers.get_board_links import get_board_link
from APP.utils.profiles import select_profile
from APP.scrapers.index_posts import index_posts




async def scrape(profile=None):
    if profile is None:
        profile = select_profile()
    # Define a semaphore to limit the number of concurrent requests
    requests_semaphore = Semaphore(profile.max_concurrent_requests)

    async for category in make_async(profile.categories):
        boards = await find_boards(category, requests_semaphore)
        async for board in make_async(boards):
            print(f"Gathering links from {category}.", end="\r")
            board_sets = [await get_board_link(board) for board in boards]
            async for set in make_async(board_sets):
                async for title, link in make_async(set):
                    await index_posts(link, category, title, requests_semaphore, profile)


async def daemon_mode():
    print("This isn't available yet.")
    pass