
from asyncio import as_completed
async def make_async(item):
    if isinstance(item, list):
        for i in item:
            if i is not None:
                yield i
    elif isinstance(item, dict):
        for k, v in item.items():
            if v is not None and k is not None:
                yield k, v

async def async_as_completed(tasks):
    for task in as_completed(tasks):
        if task is not None:
            await task
            yield task