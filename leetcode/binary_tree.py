class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

    @classmethod
    def fromlist(cls, nums):
        return cls._from_list_helper(0, nums)

    @classmethod
    def _from_list_helper(cls, index, nums):
        if index < len(nums) and nums[index]:
            return TreeNode(nums[index],
                            cls._from_list_helper(index * 2 + 1, nums),
                            cls._from_list_helper((index + 1) * 2, nums))
        else:
            return None

    def __eq__(self, other) -> bool:
        return isinstance(other, type(self))\
               and (self.val, self.left, self.right) ==\
                   (other.val, other.left, other.right)

    def __hash__(self) -> int:
        return hash((self.val, self.left, self.right))

    def __repr__(self) -> str:
        if self is None:
            return ""
        return f'{self.val} {repr(self.left)} {repr(self.right)}'
