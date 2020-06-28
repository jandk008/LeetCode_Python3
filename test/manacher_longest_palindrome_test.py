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
                                         ('aaa', 'aaa'),
                                         ('abacdedcaba', 'abacdedcaba')])
def test_find_longest_palindrome(solution: Solution, s: str, expected: str):
    assert solution.find_palindrome(s) == expected
