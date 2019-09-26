import pytest

from leetcode.is_subsequence import Solution


@pytest.fixture(autouse=True)
def solution():
    return Solution()


@pytest.mark.parametrize('s, t',
                         [('abc', 'abc'), ('ab', 'ajib'), ('', ''), ('', 'ji'),
                          ('aib', 'scabubifbsf'), ('ab', 'ssfaxab')])
def test_is_subsequence(solution: Solution, s: str, t: str):
    assert solution.is_subsequence(s, t) is True


@pytest.mark.parametrize('s, t',
                         [('ab', 'axiu'), ('ji', ''), ('sfjib', 'sjfsfib'),
                          ('a', 'biji')])
def test_is_not_subsequence(solution: Solution, s: str, t: str):
    assert solution.is_subsequence(s, t) is False
