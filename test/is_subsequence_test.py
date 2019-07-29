import pytest

from leetcode.is_subsequence import Solution


@pytest.fixture(autouse=True)
def solution():
    return Solution()


@pytest.mark.parametrize('s, t, expect',
                         [('abc', 'abc', True), ('ab', 'ajib', True),
                          ('ab', 'axiu', False), ('', '', True),
                          ('', 'ji', True), ('ji', '', False),
                          ('sfjib', 'sjfsfib', False),
                          ('aib', 'scabubifbsf', True), ('ab', 'ssfaxab', True),
                          ('a', 'biji', False)])
def test_is_subsequence(solution: Solution, s: str, t: str, expect: bool):
    assert solution.is_subsequence(s, t) == expect
