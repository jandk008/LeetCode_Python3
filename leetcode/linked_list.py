class ListNode(object):
    def __init__(self, val, _next=None):
        self.val = val
        self._next = _next

    @classmethod
    def fromlist(cls, nums):
        return cls._from_list_helper(nums, 0)

    @classmethod
    def _from_list_helper(cls, nums, index):
        if not nums or index == len(nums):
            return None
        else:
            return ListNode(nums[index], cls._from_list_helper(nums, index + 1))

    def __len__(self):
        length, current = 0, self
        while current is not None:
            length += 1
            current = current.next
        return length

    def __eq__(self, o: object) -> bool:
        return isinstance(o, type(self)) \
               and self.val == o.val and self._next == o._next

    def __hash__(self) -> int:
        return hash((self.val, self._next))

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, _next):
        self._next = _next
