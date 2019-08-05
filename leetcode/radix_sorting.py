class RadixSorting:
    def sort(self, nums) -> list:
        maximum, digit = max(nums), 1
        while maximum:
            nums = self._count_sort(nums, digit)
            digit *= 10
            maximum //= digit
        return list(nums)

    def _count_sort(self, nums, digit):
        counts = [0] * 10
        _sorted = [0] * len(nums)
        for num in nums:
            counts[(num // digit) % 10] += 1
        for i in range(1, len(counts)):
            counts[i] += counts[i - 1]
        for num in nums[::-1]:
            _sorted[counts[(num // digit) % 10] - 1] = num
            counts[(num // digit) % 10] -= 1
        return _sorted
