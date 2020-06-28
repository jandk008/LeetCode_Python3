import asyncio
import random
import time
from typing import Any


async def sub_foo(parent_id: int):
    random_number = random.randint(1, 3)
    print(f'start to run sub_foo for {parent_id} '
          f'and sleep for {random_number} seconds')
    return await asyncio.sleep(random_number, 2)


async def foo(task_id: int):
    print(f'start to run foo in task {task_id}')
    now = time.perf_counter()
    random_number = 3 - task_id
    print(f'task {task_id} sleep for {random_number} seconds')
    await asyncio.sleep(random_number)
    complete_sleeping = time.perf_counter() - now
    print(f'task {task_id} completed sleep with {complete_sleeping}')
    result = await sub_foo(task_id)
    print(f'Got result which is {result} in task {task_id} '
          f'within {time.perf_counter() - now} seconds')


async def async_generator():
    for _ in range(10):
        yield _


def sync_generator():
    for _ in range(10):
        yield _


async def main():
    now = time.perf_counter()
    async for _ in async_generator():
        print(f'async generator value is {_}')
    print(f'completed in {time.perf_counter() - now:.8f}')
    # await print_hello()
    # await print_world()
    # print(f'complete printing hello world in {time.perf_counter() - now}')


async def print_hello():
    print('hello')


async def print_world():
    print('world')


class Foo:

    def __init__(self):
        self.map = {}

    def __setitem__(self, key, value) -> None:
        print(f'key {key} is with value {value}')
        self.map[key] = value

    def __getitem__(self, item) -> Any:
        print(f'item is {item}')
        return self.map[item]

    def __call__(self, *args, **kwargs):
        print(f'being called with {args}')


if __name__ == '__main__':
    f = Foo()
    f['name'] = 'zidane'
    print(f['name'])
    f(2)
    # asyncio.run(main())


