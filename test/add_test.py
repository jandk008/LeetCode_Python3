import asyncio

import pytest
import typing

from leetcode.add import Additor


@pytest.mark.parametrize("a,b,expected", [(1, 2, 3), (2, 3, 5)])
def test_add(a, b, expected):
    test_logging(a, b)
    test_person()
    # asyncio.run(main())
    print('type of based is', type(based()))
    print('type of native is', type(native()))
    assert Additor.add(a, b) == expected


async def generator():
    return 1, 2, 3


@asyncio.coroutine
def based():
    yield 1, 2, 3


@asyncio.coroutine
def native():
    yield from based()


def logging(log_level=None):
    def wrap_logging(func):
        def wrapper(*args):
            print(f'target log level is {"warn".lower()} passed log level is'
                  f' {log_level}')
            if log_level == 'warn'.lower():
                print(f'hi, this logging function to start\nargs is {args}')
                func(*args)
                print('logging finished')
            else:
                print('only log with log level of warn')

        return wrapper

    return wrap_logging


class Person(object):
    def __init__(self, name):
        self._name = name

    def __repr__(self):
        return self.name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def lower(self):
        return self.name.lower()


@logging('warn')
def test_logging(a=1, b=2):
    person = Person('zidn')
    person.name = 'ji'
    print(f'{person.name}')
    print(f'{sum([a, b])}')
    with execute('zidane') as manager:
        manager.impromptu('yell')


def test_person():
    persons = [Person("zidane"), Person("rooney")]
    persons.sort(key=Person.lower)
    print(persons)
    strs = ["heel", "xuvi", "abuisd"]
    strs.sort(key=str.lower)
    print(strs)


def execute(name):
    return MyContextManager(name)


class MyContextManager(object):
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print(f'Entering to {self.name}')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"exception type: {exc_type} \n exception value: {exc_val} \n "
              f"exception traceback: {exc_tb}")
        print(f'Exiting the {self.name}')

    def impromptu(self, act):
        print(f"I'm doing {act} on {self.name}")

def test_foo():
    solution = Solution()
    print(solution.partition('aab'))

class Solution:
    def partition(self, s: str):
        lists = []
        self._partition(s, 0, [], lists)
        return lists

    def _partition(self, s, index, palindrome, lists):
        if index == len(s):
            lists.append(list(palindrome))
        else:
            for _ in range(index, len(s)):
                if self.isPalindromic(s, index, _):
                    palindrome.append(s[index:_ + 1])
                    self._partition(s, _ + 1, palindrome, lists)
                    del palindrome[-1]

    def isPalindromic(self, s, start, end):
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True

from typing import Union, Optional, List, Any, Dict

class LogProcess(typing.Protocol):
    def __call__(
        self,
        cmd: typing.Union[str, typing.List[str]],
        name: typing.Optional[str] = None,
        out_level: Optional[int] = None,
        err_level: Optional[int] = None,
        popen_posargs: Optional[List[Any]] = None,
        popen_kwargs: Optional[Dict[str, Any]] = None,
    ) -> None:
        pass

def log_process(
    cmd: Union[str, List[str]],
    *,
    name: Optional[str] = None,
    out_level: int = logging.INFO,
    err_level: int = logging.WARNING,
    popen_posargs: Optional[List[Any]] = None,
    popen_kwargs: Optional[Dict[str, Any]] = None,
) -> None:
