import pytest

from leetcode.radix_sorting import RadixSorting


@pytest.fixture()
def radix_sorting():
    return RadixSorting()


@pytest.mark.parametrize("nums, expected", [([3, 1, 2], [1, 2, 3]), (
    [21, 34, 15, 51, 35235, 124, 5], [5, 15, 21, 34, 51, 124, 35235]), (
                                                [3, 44, 3, 2, 1, 8],
                                                [1, 2, 3, 3, 8, 44])])
def test_radix_sorting(radix_sorting: RadixSorting, nums: list, expected: list):
    assert radix_sorting.sort(nums) == expected
