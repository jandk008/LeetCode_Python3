from leetcode.binary_tree import TreeNode


class Solution:
    def insert(self, root: TreeNode, node: int) -> TreeNode:
        if not root:
            return TreeNode(node)
        if root.val < node:
            root.right = self.insert(root.right, node)
        elif root.val > node:
            root.left = self.insert(root.left, node)
        else:
            return root
        return self.rotate(root, node)

    def delete(self, root: TreeNode, node: int) -> TreeNode or None:
        if not root:
            return root
        if root.val == node:
            if root.left is None and root.right is None:
                return None
            elif bool(root.right is None) ^ bool(root.left is None):
                return root.left if root.right is None else root.right
            else:
                successor = self.get_successor(root.right)
                root.val = successor
                root.right = self.delete(root.right, successor)
        elif root.val < node:
            root.right = self.delete(root.right, node)
        else:
            root.left = self.delete(root.left, node)
        return self.rotate_delete(root)

    def rotate(self, root, node):
        self.update_height(root)
        balance_indicator = self.get_balance_indicator(root)
        if balance_indicator > 1:
            if node < root.left.val:
                root = self.rotate_right(root)
            else:
                root.left = self.rotate_left(root.left)
                root = self.rotate_right(root)
        elif balance_indicator < -1:
            if node > root.right.val:
                root = self.rotate_left(root)
            else:
                root.right = self.rotate_right(root.right)
                root = self.rotate_left(root)
        return root

    def update_height(self, root):
        if root:
            root.height = self.get_height(root)

    def get_height(self, root):
        if not root:
            return 0
        return 1 + max(self.get_height(root.left), self.get_height(root.right))

    @staticmethod
    def get_balance_indicator(root):
        left_height = root.left.height if root.left else 0
        right_height = root.right.height if root.right else 0
        return left_height - right_height

    def rotate_left(self, root):
        new_root = root.right
        root.right = new_root.left
        new_root.left = root

        self.update_height(root)
        self.update_height(new_root)
        return new_root

    def rotate_right(self, root):
        new_root = root.left
        root.left = new_root.right
        new_root.right = root

        self.update_height(root)
        self.update_height(new_root)
        return new_root

    def rotate_delete(self, root):
        self.update_height(root)
        balance_indicator = self.get_balance_indicator(root)
        if balance_indicator > 1:
            if self.get_balance_indicator(root.left) < 0:
                root.left = self.rotate_left(root.left)
            root = self.rotate_right(root)
        elif balance_indicator < -1:
            if self.get_balance_indicator(root.right) > 0:
                root.right = self.rotate_right(root.right)
            root = self.rotate_left(root)
        return root

    @staticmethod
    def get_successor(root):
        while root.left:
            root = root.left
        return root.val
