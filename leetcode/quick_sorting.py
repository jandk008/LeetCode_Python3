class Solution:
    def sort(self, nums):
        self._quick_sort_helper(nums, 0, len(nums) - 1)

    def _quick_sort_helper(self, nums, low, high):
        if low > high:
            return
        pivot = nums[low]
        left = low + 1
        right = high
        while left < right:
            while left < right and nums[left] <= pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
        if pivot > nums[right]:
            nums[low], nums[right] = nums[right], nums[low]
        self._quick_sort_helper(nums, low, right - 1)
        self._quick_sort_helper(nums, left, high)
