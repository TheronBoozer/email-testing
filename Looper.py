import asyncio

from main import random_email


async def periodic():
    while True:
        print('periodic')
        await random_email()
        await asyncio.sleep(5*60)

def stop():
    task.cancel()

loop = asyncio.get_event_loop()
# loop.call_later(5, stop)
task = loop.create_task(periodic())

try:
    loop.run_until_complete(task)
except asyncio.CancelledError:
    pass