import collections


class Solution(object):
    def longestPalindrome(self, s: str) -> int:
        count = collections.Counter(s)
        longest, has_odd_count = 0, False
        for key in count:
            if count[key] % 2 == 0:
                longest += count[key]
            else:
                has_odd_count = True
                longest += count[key] - 1
        return longest + 1 if has_odd_count else longest
