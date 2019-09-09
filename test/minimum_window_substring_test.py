import pytest

from leetcode.minimum_window_substring import Solution


@pytest.fixture()
def solution():
    return Solution()


@pytest.mark.parametrize("s, t, expected", [("ADOBECODEBANC", "ABC", "BANC"),
                                            ("ADOBECBANC", "ABC", "CBA"),
                                            ("AAAABBBCDDD", "DBBC", "BBCD"),
                                            ("ADOBECODEBANC", "BX", "")])
def test_minimum_window_substring(solution: Solution, s: str, t: str, expected):
    assert solution.min_window(s, t) == expected
