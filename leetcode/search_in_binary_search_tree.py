from leetcode.binary_tree import TreeNode


class Solution(object):
    def searchBST(self, root: TreeNode, value: int) -> TreeNode:
        if not root or root.val == value:
            return root
        else:
            return self.searchBST(root.left, value) \
                if root.val > value \
                else self.searchBST(root.right, value)
