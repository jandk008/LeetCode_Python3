class Solution:

    @staticmethod
    def find_palindrome(s: str) -> str:
        n = 2 * len(s) + 1
        lps = [0] * n
        lps[1] = 1
        max_index, max_length, center, i = 1, 3, 1, 2
        while i < n:
            left, right = 2 * center - i, center + lps[center]
            length = lps[left]
            if lps[left] >= right - i:
                length = right - i
                l, r = i - length - 1, i + length + 1
                while l >= 0 and r < n and (l % 2 == 0 or s[l // 2] == s[r // 2]):
                    length, l, r = length + 2, l - 1, r + 1
            lps[i] = length
            if length > max_length:
                max_index, max_length = i, lps[i]
            i += 1
            if i > right:
                center = i
        start = (max_index - max_length // 2) // 2
        return s[start: start + max_length // 2]
