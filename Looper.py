import asyncio

from main import random_email
from selenium_sadness import ask_gpt


async def periodic():
    while True:
        print('periodic')
        await random_email()
        await asyncio.sleep(5*60)

def stop():
    for task in tasks:
        task.cancel()

loop = asyncio.get_event_loop()
# loop.call_later(5, stop)
tasks = []
tasks.append(loop.create_task(periodic()))
# tasks.append(loop.create_task(ask_gpt()))

try:
    loop.run_until_complete(tasks[0])
    # loop.run_until_complete(ask_gpt)
except asyncio.CancelledError:
    pass