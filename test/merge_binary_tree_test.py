import math

import pytest

from leetcode.binary_tree import TreeNode
from leetcode.merge_binary_tree import Solution


@pytest.fixture()
def solution():
    return Solution()


@pytest.mark.parametrize("t1, t2, expected",
                         [(TreeNode.fromlist([1, 3, 2, 5]),
                           TreeNode.fromlist([2, 1, 3, None, 4, None, 7]),
                           TreeNode.fromlist([3, 4, 5, 5, 4, None, 7])),
                          (TreeNode.fromlist([1, 2, 3]),
                           TreeNode.fromlist([1, 2, 3, 4, 5, 6]),
                           TreeNode.fromlist([2, 4, 6, 4, 5, 6])),
                          (TreeNode.fromlist([1]), TreeNode.fromlist([]),
                           TreeNode.fromlist([1]))])
def test_merge_binary_tree(solution: Solution, t1, t2, expected):
    assert solution.merge_binary_tree(t1, t2) == expected


def test():
    foo(2, t=2, name='hi')
    a = [1, 2, 3]
    b = [3, 4, 5]
    print([*a, *b])
    assert gcd(24, 16) == 8
    assert math.sqrt(9) == 3


def foo(k, *, t, name=None):
    print(f'k: {k}, t: {t}, name: {name}')


def gcd(x, y):
    while y:
        x, y = y, x % y
    return x
