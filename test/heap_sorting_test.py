import pytest

from leetcode.heap_sorting import Solution


@pytest.fixture()
def solution():
    return Solution()


@pytest.mark.parametrize('nums, expected',
                         [([2, 2, 1], [1, 2, 2]), ([1], [1]), ([1, 2], [1, 2]),
                          ([4, 3, 2, 1], [1, 2, 3, 4]), ([33, 22], [22, 33]),
                          ([2, 3, 4, 3, 5, 2, 7], [2, 2, 3, 3, 4, 5, 7]),
                          ([1, 2, 1, 2, 1], [1, 1, 1, 2, 2]),
                          ([1, 2, 3], [1, 2, 3]), (
                              [1, 2324, 14, 21, 12, 132, 34, 512, 5, 24],
                              [1, 5, 12, 14, 21, 24, 34, 132, 512, 2324])])
def test_quick_sorting(solution: Solution, nums: list, expected: list):
    solution.sort(nums)
    assert nums == expected
