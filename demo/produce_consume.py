import asyncio
import random
import time


async def random_sleep(caller=None):
    seconds = random.randint(0, 3)
    if caller:
        print(f'{caller} is sleeping for {seconds} seconds')
    await asyncio.sleep(seconds)


async def consume(name: str, queue: asyncio.Queue) -> None:
    while True:
        print(f'{name} consumer starts to consume')
        t, message = await queue.get()
        now = time.perf_counter()
        print(f'{name} consumer consumed {message} in {now - t:.2f} seconds')
        queue.task_done()
        await random_sleep(caller=f'consumer {name}')


async def produce(name: str, queue: asyncio.Queue) -> None:
    print(f'{name} producer starts to produce messages')
    message_count = random.randint(0, 10)
    for _ in range(message_count):
        await asyncio.sleep(random.randint(0, 3))
        message = f'{_} message coming from {name} producer'
        now = time.perf_counter()
        await queue.put((now, message))
        print(f'{name} producer published \'{message}\' to the queue')


async def producer_consumer_demo():
    queue = asyncio.Queue()
    producers = [asyncio.create_task(produce(_, queue)) for _ in range(2)]
    consumers = [asyncio.create_task(consume(_, queue)) for _ in range(5)]

    await asyncio.gather(*producers)
    await queue.join()
    for c in consumers:
        c.cancel()
    print(f'Demo is over')


if __name__ == '__main__':
    asyncio.run(producer_consumer_demo())
