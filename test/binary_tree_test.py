import pytest

from leetcode.binary_tree import TreeNode


@pytest.mark.parametrize("nums", [(1, 2, 3, 5, None, 4, None, 6)])
def test_binary_tree_node_from_list(nums: list):
    node6 = TreeNode(nums[7])
    node4 = TreeNode(nums[5])
    node5 = TreeNode(nums[3], node6)
    node2 = TreeNode(nums[1], node5)
    node3 = TreeNode(nums[2], node4)
    assert TreeNode.fromlist(nums) == TreeNode(nums[0], node2, node3)
