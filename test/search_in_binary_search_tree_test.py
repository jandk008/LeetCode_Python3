import pytest

from leetcode.binary_tree import TreeNode
from leetcode.search_in_binary_search_tree import Solution


@pytest.fixture()
def solution():
    return Solution()


@pytest.mark.parametrize("root, value, expected", [
    (TreeNode.fromlist([4, 2, 7, 1, 3]), 2, TreeNode.fromlist([2, 1, 3])),
    (TreeNode.fromlist([4, 2, 7, 1, 3]), 5, None), (None, 5, None),
    (TreeNode.fromlist([4, 2, 7, 1, 3]), 2, TreeNode.fromlist([2, 1, 3]))])
def test_search_in_binary_search_tree(solution: Solution, root: TreeNode,
                                      value: int, expected: TreeNode):
    assert solution.searchBST(root, value) == expected
