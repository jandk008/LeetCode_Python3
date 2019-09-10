import pytest

from leetcode.asteroid_collision import Solution


@pytest.fixture()
def solution():
    return Solution()


@pytest.mark.parametrize("asteroids, expected",
                         [([8, -8], []), ([10, 2, -5], [10]),
                          ([-2, -1, 1, 2], [-2, -1, 1, 2]), ([8], [8]),
                          ([5, 10, -5], [5, 10])])
def test_asteroid_collision(solution: Solution, asteroids, expected):
    assert solution.asteroid_collision(asteroids) == expected
