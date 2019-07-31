import pytest

from leetcode.binary_tree import TreeNode
from leetcode.binary_tree_right_side_view import Solution


@pytest.fixture()
def solution():
    return Solution()


@pytest.mark.parametrize("nums, expected",
                         [([1, 2, 3, None, 5, None, 4], [1, 3, 4]),
                          ([1, 2, 3, 5, None, 4, None, 6], [1, 3, 4, 6])])
def test_binary_tree_right_side_view(solution, nums, expected):
    assert solution.rightSideView(TreeNode.fromlist(nums)) == expected
