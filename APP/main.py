
from asyncio import run


from APP.utils.menu import main_menu



async def main():
    await main_menu()




if __name__ == '__main__':
    run(main())