
from APP.config import base_urls

async def get_board_link(board):
    board_title = board.find(class_="linkName").text
    board_url = board.find(class_="linkReply")["href"]
    return {board_title:board_url}


