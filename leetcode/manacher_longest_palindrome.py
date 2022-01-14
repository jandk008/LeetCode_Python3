class Solution:

    @staticmethod
    def find_palindrome(s: str) -> str:
        A = '^#' + '#'.join(s) + '#$'
        n = len(A)
        lps = [0] * n
        max_index = max_length = right = center = 0
        for i in range(1, n - 1):
            if i < right:
                lps[i] = min(right - i, lps[2 * center - i])
            while A[i - lps[i] - 1] == A[i + lps[i] + 1]:
                lps[i] += 1
            if i + lps[i] > right:
                center, right = i, i + lps[i]
            if lps[i] > max_length:
                max_index, max_length = i, lps[i]
        start = (max_index - max_length) // 2
        return s[start: start + max_length]
