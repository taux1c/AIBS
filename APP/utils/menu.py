
import webbrowser


from APP.utils.profiles import select_profile, create_profile
from APP.scrapers.scrape import scrape, daemon_mode
from APP.utils.download import download


async def scrape_and_download():
    profile = select_profile()
    await scrape(profile)
    await download(profile)


async def edit_profile():
    profile = select_profile()
    profile.edit()

async def open_github_site():
    try:
        webbrowser.open('https://github.com/taux1c/AIBS')
    except:
        print('Failed to open github site but you can find it here: https://github.com/taux1c/AIBS')

async def adjust_request_rate():
    profile = select_profile()
    profile.set_request_rate()
async def close_app():
    quit()
async def main_menu():
    try:
        webbrowser.open('https://www.buymeacoffee.com/taux1c')
    except:
        pass
    options = {
        '1': create_profile,
        '2': edit_profile,
        '3': scrape,
        '4': download,
        '5': scrape_and_download,
        '6': daemon_mode,
        '7': open_github_site,
        '8': adjust_request_rate,
        '9': close_app
    }
    while True:
        for key, value in options.items():
            print(f'{key}: {value.__name__}')
        choice = input('Enter your choice: ')
        if choice not in options.keys():
            print('Invalid choice.\nPlease try again.')
        else:
            break
    if choice is not None:
        try:
            await options[choice]()
        except:
            raise

