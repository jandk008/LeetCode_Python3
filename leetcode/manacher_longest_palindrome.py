class Solution:

    @staticmethod
    def find_palindrome(s: str) -> str:
        n = 2 * len(s) + 1
        lps = [0] * n
        lps[1] = 1
        max_index, max_length, center, i = 1, 1, 1, 2
        for i in range(n):
            left, right = 2 * center - i, center + lps[center]
            length = lps[left] if left >= 0 else 0
            if i + length >= right:
                length = right - i
                l, r = i - length - 1, i + length + 1
                while l >= 0 and r < n and (l % 2 == 0 or s[l // 2] == s[r // 2]):
                    length, l, r = length + 1, l - 1, r + 1
                center = i
                if length > max_length:
                    max_index, max_length = i, length
            lps[i] = length
        start = (max_index - max_length) // 2
        return s[start: start + max_length]
