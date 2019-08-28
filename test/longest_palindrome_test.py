import pytest

from leetcode.longest_palindrome import Solution


@pytest.fixture()
def solution():
    return Solution()


@pytest.mark.parametrize("s, expected",
                         [("abccccdd", 7), ("", 0), ("a", 1), ("abbaacdde", 7),
                          ("abbbaaddd", 7), ("aaaabcccc", 9), (
                          "zeusnilemacaronimaisanitratetartinasiaminoracamelinsuez",
                          55)])
def test_longest_palindrome(solution: Solution, s: str, expected: int):
    assert solution.longestPalindrome(s) == expected
