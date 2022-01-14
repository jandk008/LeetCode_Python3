import pytest

from leetcode.temp_avl_binary_search_tree import Solution
from leetcode.binary_tree import TreeNode


@pytest.fixture()
def solution():
    return Solution()


@pytest.mark.parametrize("tree, node, expected", [
    (TreeNode.fromlist([]), 3, TreeNode.fromlist([3])),
    (TreeNode.fromlist([2, 1]), 3, TreeNode.fromlist([2, 1, 3])),
    (TreeNode.fromlist([2, 1, 3]), 4,
     TreeNode.fromlist([2, 1, 3, None, None, None, 4])),
    (TreeNode.fromlist([2, 1, 5, None, None, 3]), 7,
     TreeNode.fromlist([2, 1, 5, None, None, 3, 7])),
    (TreeNode.fromlist([3, 2]), 1, TreeNode.fromlist([2, 1, 3])),
    (TreeNode.fromlist([1, None, 2]), 3, TreeNode.fromlist([2, 1, 3])),
    (TreeNode.fromlist([5, 2, 6, 1, 3]), 4,
     TreeNode.fromlist([3, 2, 5, 1, None, 4, 6])),
    (TreeNode.fromlist([5, 2, 8, None, None, 7, 9]), 6,
     TreeNode.fromlist([7, 5, 8, 2, 6, None, 9]))])
def test_avl_binary_search_tree_insert(
        solution: Solution, tree: TreeNode, node: int, expected: TreeNode):
    assert solution.insert(tree, node) == expected


@pytest.mark.parametrize("tree, node, expected", [
    (TreeNode.fromlist([2, 1, 3]), 3, TreeNode.fromlist([2, 1])),
    (TreeNode.fromlist([2, 1, 3]), 2, TreeNode.fromlist([3, 1])),
    (TreeNode.fromlist([3, 2, 4, 1]), 2, TreeNode.fromlist([3, 1, 4])),
    (TreeNode.fromlist([3, 2, 4, 1]), 4, TreeNode.fromlist([2, 1, 3])),
    (TreeNode.fromlist([7, 3, 9, 2, 5, 8, 10, None, None, 4, 6]), 3,
     TreeNode.fromlist([7, 4, 9, 2, 5, 8, 10, None, None, None, 6])),
    (TreeNode.fromlist([3, 2, 4, None, None, None, 5]), 2,
     TreeNode.fromlist([4, 3, 5])),
    (TreeNode.fromlist([8, 2, 9, 1, 4, None, 10, None, None, 3, 5]), 10,
     TreeNode.fromlist([4, 2, 8, 1, 3, 5, 9])),
    (TreeNode.fromlist([2, 1, 6, 0, None, 4, 7, None, None, None, None, 3]), 0,
     TreeNode.fromlist([4, 2, 6, 1, 3, None, 7])),
    (TreeNode.fromlist([4, 3, 5, 2, None, None, 6, 1]), 5,
     TreeNode.fromlist([3, 2, 4, 1, None, None, 6])),
    (TreeNode.fromlist([4, 3, 5, 2, None, None, 6, 1]), 3,
     TreeNode.fromlist([4, 2, 5, 1, None, None, 6])),
    (TreeNode.fromlist([8, 5, 11, 4, 7, 10, None, 3, None, 6]), 8,
     TreeNode.fromlist([5, 4, 10, 3, None, 7, 11, None, None, None, None, 6])),
    (TreeNode.fromlist([4, 2, 5, 1, 3]), 2, TreeNode.fromlist([4, 3, 5, 1]))])
def test_avl_binary_search_tree_delete(
        solution: Solution, tree: TreeNode, node: int, expected: TreeNode):
    assert solution.delete(tree, node) == expected
