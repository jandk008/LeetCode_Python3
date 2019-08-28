class Solution(object):
    def hasAlternatingBits(self, num: int) -> bool:
        m = num ^ (num >> 1)
        return not (m & (m + 1))
