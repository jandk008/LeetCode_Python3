import pytest

from leetcode.trapping_rain_water_II import Solution


@pytest.fixture()
def solution():
    return Solution()


@pytest.mark.parametrize("heights, expected", [
    ([[1, 4, 3, 1, 3, 2], [3, 6, 5, 3, 2, 4], [2, 3, 3, 2, 3, 1]], 1),
    ([[1, 4, 3, 1, 3, 2], [3, 3, 3, 3, 3, 4], [2, 3, 3, 2, 3, 1]], 0),
    ([[]], 0), ([], 0),
    ([[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]], 4)])
def test_trapping_rain_water(solution, heights, expected):
    assert solution.trapRainWater(heights) == expected
