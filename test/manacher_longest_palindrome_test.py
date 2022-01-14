import bisect

import pytest

from leetcode.manacher_longest_palindrome import Solution


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize('s, expected', [('ababa', 'ababa'), ('abba', 'abba'),
                                         ('babcbabcbaccba', 'abcbabcba'),
                                         ('abaaba', 'abaaba'), ('caba', 'aba'),
                                         ('abababa', 'abababa'), ('a', 'a'),
                                         ('abcbabcbabcba', 'abcbabcbabcba'),
                                         ('forgeeksskeegfor', 'geeksskeeg'),
                                         ('abacdfgdcaba', 'aba'), ('aa', 'aa'),
                                         ('abacdfgdcabba', 'abba'),
                                         ('aab', 'aa'), ('babad', 'bab'),
                                         ('aaa', 'aaa'), ('aba', 'aba'),
                                         ('abacdedcaba', 'abacdedcaba')])
def test_find_longest_palindrome(solution: Solution, s: str, expected: str):
    # assert solution.find_palindrome(s) == expected
    print(pow(2, 8))


def pow(x, n):
    while n > 0:
        if n % 2:
            x += x
        else:
            x *= x
        n >>= 1
    return x


@pytest.mark.parametrize('nums, val, expected',
                         [([1, 2], 2, 1), ([1, 2, 3, 4, 5], 3, 2),
                          ([1, 2, 3, 4, 4, 5, 6, 7, 8, 9], 8, 8),
                          ([1, 2, 2, 3, 3, 5], 4, 5), ([1, 2, 3], 0, 0)])
def test_bst(nums: list, val: int, expected: int):
    assert bst_1(nums, val) == expected
    assert bst_2(nums, val) == expected
    assert bisect.bisect_left(nums, val) == expected


def bst_1(nums, val):
    l, r = 0, len(nums) - 1
    while l < r:
        mid = l + (r - l) // 2
        if nums[mid] >= val:
            r = mid
        else:
            l = mid + 1
    return l

def bst_2(nums, val):
    l, r = 0, len(nums)
    while l < r:
        mid = l + (r - l) // 2
        if nums[mid] >= val:
            r = mid
        else:
            l = mid + 1
    return l
