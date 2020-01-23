class TreeNode(object):
    def __init__(self, x, left=None, right=None, height=1):
        self.val = x
        self.left = left
        self.right = right
        self.height = height

    @classmethod
    def fromlist(cls, nums):
        return cls._from_list_helper(0, nums)

    @classmethod
    def _from_list_helper(cls, index, nums):
        if index < len(nums) and nums[index]:
            left = cls._from_list_helper(index * 2 + 1, nums)
            right = cls._from_list_helper((index + 1) * 2, nums)
            height = 1 + max(cls.get_height(left), cls.get_height(right))
            return TreeNode(nums[index], left, right, height)
        else:
            return None

    @staticmethod
    def get_height(root):
        if not root:
            return 0
        return root.height

    def __eq__(self, other) -> bool:
        return isinstance(other, type(self))\
               and (self.val, self.left, self.right, self.height) ==\
                   (other.val, other.left, other.right, self.height)

    def __hash__(self) -> int:
        return hash((self.val, self.left, self.right, self.height))

    def __repr__(self) -> str:
        if self is None:
            return ""
        return \
            f'{self.val} {repr(self.left)} {repr(self.right)} {repr(self.height)}'
