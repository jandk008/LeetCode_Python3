import pytest

from leetcode.string_compression import Solution


@pytest.fixture()
def solution():
    return Solution()


@pytest.mark.parametrize("string, expected",
                         [(['a'], 1), (['a', 'a', 'a', 'b', 'b', 'b'], 4),
                          ([], 0), (['a', 'b', 'c', 'c', 'c', 'd'], 5),
                          (['a', 'a', 'b', 'b', 'c', 'c', 'c'], 6), (
                          ['a', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b',
                           'b', 'b', 'b'], 4)])
def test_string_compression(solution, string, expected):
    assert solution.compress(string) == expected
