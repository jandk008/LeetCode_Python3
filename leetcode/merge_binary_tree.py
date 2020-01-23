from leetcode.binary_tree import TreeNode


class Solution(object):
    def merge_binary_tree(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 is None:
            return t2
        elif t2 is None:
            return t1
        else:
            return TreeNode(t1.val + t2.val,
                            self.merge_binary_tree(t1.left, t2.left),
                            self.merge_binary_tree(t1.right, t2.right))
