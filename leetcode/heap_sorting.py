class Solution:
    def sort(self, nums: list):
        self._construct(nums)
        for _ in range(len(nums))[::-1]:
            nums[_], nums[0] = nums[0], nums[_]
            self._heapify(nums, 0, _)

    def _construct(self, nums):
        for _ in range(len(nums))[::-1]:
            self._heapify(nums, _, len(nums))

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
