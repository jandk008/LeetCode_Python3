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
            if bool(root.right is None) ^ bool(root.left is None):
                return root.right if root.left is None else root.left
            successor = self.find_successor(root.right)
            root.val = successor.val
            root.right = self.delete(root.right, successor.val)
        elif root.val < node:
            root.right = self.delete(root.right, node)
        else:
            root.left = self.delete(root.left, node)

        root.height = self.update_height(root)
        balance_factor = self.get_balance(root)

        if balance_factor < -1:
            if self.get_balance(root.left) > 0:
                root.left = self.left_rotation(root.left)
            root = self.right_rotation(root)
        elif balance_factor > 1:
            if self.get_balance(root.right) < 0:
                root.right = self.right_rotation(root.right)
            root = self.left_rotation(root)
        return root

    def get_balance(self, root):
        return self.get_height(root.right) - self.get_height(root.left)

    def rotate(self, root, node):
        root.height = self.update_height(root)
        balance_factor = self.get_balance(root)
        if balance_factor < -1:
            if node < root.left.val:
                root = self.right_rotation(root)
            else:
                root.left = self.left_rotation(root.left)
                root = self.right_rotation(root)
        elif balance_factor > 1:
            if node > root.right.val:
                root = self.left_rotation(root)
            else:
                root.right = self.right_rotation(root.right)
                root = self.left_rotation(root)
        return root

    @staticmethod
    def get_height(root: TreeNode) -> int:
        return root.height if root else 0

    def right_rotation(self, root):
        if not root:
            return root
        new_root = root.left
        root.left = new_root.right
        new_root.right = root

        root.height = self.update_height(root)
        new_root.height = self.update_height(new_root)

        return new_root

    def left_rotation(self, root):
        if not root:
            return root
        new_root = root.right
        root.right = new_root.left
        new_root.left = root

        root.height = self.update_height(root)
        new_root.height = self.update_height(new_root)

        return new_root

    def update_height(self, root):
        return 1 + max(self.get_height(root.left), self.get_height(root.right))

    @staticmethod
    def find_successor(root) -> TreeNode:
        while root.left:
            root = root.left
        return root
