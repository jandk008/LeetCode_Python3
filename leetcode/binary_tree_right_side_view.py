from leetcode.binary_tree import TreeNode


class Solution(object):
    def rightSideView(self, root: TreeNode) -> list:
        right_nodes_each_level = {}
        self._find_right_views_child(root, 1, right_nodes_each_level)
        return list(right_nodes_each_level.values())

    def _find_right_views_child(self, root: TreeNode, level: int,
                                level_map: dict):
        if not root:
            return
        if level not in level_map:
            level_map[level] = root.val
        self._find_right_views_child(root.right, level + 1, level_map)
        self._find_right_views_child(root.left, level + 1, level_map)
