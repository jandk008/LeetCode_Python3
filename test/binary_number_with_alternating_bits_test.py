import pytest

from leetcode.binary_number_with_alternating_bits import Solution


@pytest.fixture()
def solution():
    return Solution()


@pytest.mark.parametrize("num", [1, 2, 5, 10])
def test_binary_number_with_alternating_bits(solution: Solution, num):
    assert solution.hasAlternatingBits(num)


@pytest.mark.parametrize("num", [3, 4, 6, 7, 8, 9, 11])
def test_binary_number_without_alternating_bits(solution: Solution, num):
    assert not solution.hasAlternatingBits(num)
