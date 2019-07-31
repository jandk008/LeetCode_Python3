import pytest

from leetcode.binary_tree import TreeNode
from leetcode.binary_tree_right_side_view import Solution


@pytest.fixture()
def solution():
    return Solution()


@pytest.mark.parametrize("root, expected", [
    (TreeNode.fromlist([1, 2, 3, None, 5, None, 4]), [1, 3, 4]),
    (TreeNode.fromlist([1, 2, 3, 5, None, 4, None, 6]), [1, 3, 4, 6])])
def test_binary_tree_right_side_view(solution, root, expected):
    assert solution.rightSideView(root) == expected
