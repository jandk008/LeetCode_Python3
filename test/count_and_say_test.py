import pytest

from leetcode.count_and_say import Solution


@pytest.fixture(scope='function', autouse=True)
def solution():
    yield Solution()


@pytest.mark.parametrize("n,expected",
                         [(1, '1'), (2, '11'), (3, '21'), (4, '1211'),
                          (5, '111221'), (8, '1113213211')])
def test_count_and_say(solution, n, expected):
    assert solution.count_and_say(n) == expected
