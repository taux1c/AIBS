
from asyncio import get_event_loop, wait


from AIBS.functions.create_account import Create_account
from AIBS.functions.Login_to_account import Login_to_account
from AIBS.functions.scrape_custom_url import Scrape_Custom_url
from AIBS.functions.scrape_favorites import Scrape_favorites
from AIBS.functions.edit_favorites import Edit_favorites
from AIBS.functions.edit_account import Edit_account
from AIBS.functions.download_content import Download_content
from AIBS.functions.daemon_mode import Daemon_mode
from AIBS.functions.close_app import Close_app





def main_menu():
    selections = {
        '1': Create_account,
        '2': Login_to_account,
        '3': Scrape_Custom_url,
        '4': Scrape_favorites,
        '5': Edit_favorites,
        '6': Edit_account,
        '7': Download_content,
        '8': Daemon_mode,
        '9': Close_app,
    }
    while True:
        for key, value in selections.items():
            print(key, value.__name__.replace('_', ' ').title())
        selection = input('Please select an option: ')
        if selection in selections:
            top_tasks = []
            loop = None
            try:
                loop = get_event_loop()
                top_tasks.append(loop.create_task(selections[selection]()))
                loop.run_until_complete(wait(top_tasks))
                break
            except KeyboardInterrupt:
                if loop is not None:
                    loop.close()
                break
            except Exception as e:
                print(e)
                if loop is not None:
                    loop.close()
                break
            finally:
                if loop is not None:
                    loop.close()
        else:
            print('Invalid selection')

if __name__ == '__main__':
    main_menu()
