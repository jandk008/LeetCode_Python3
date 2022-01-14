class Solution:
    def sort(self, nums: list):
        n = len(nums)
        self._construct(nums)
        for pos in range(n - 1, -1, -1):
            nums[pos], nums[0] = nums[0], nums[pos]
            self._heapify(nums, 0, pos)

    def _construct(self, nums):
        n = len(nums)
        for i in range(n - 1, -1, -1):
            self._heapify(nums, i, n)

    def _heapify(self, nums, index, end):
        swap_index = index

        left = index * 2 + 1
        if left < end:
            swap_index = left if nums[left] > nums[swap_index] else swap_index

        right = (index + 1) * 2
        if right < end:
            swap_index = right if nums[right] > nums[swap_index] else swap_index

        if swap_index != index:
            nums[swap_index], nums[index] = nums[index], nums[swap_index]
            self._heapify(nums, swap_index, end)
