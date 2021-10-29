class Solution:
    @staticmethod
    def kmp_search(s: str, p: str) -> int:
        m, n = len(p), len(s)
        lps = Solution.construct_longest_prefix_suffix(p, m)

        i = j = 0
        while i < n:
            if p[j] == s[i]:
                j += 1
                i += 1
            elif j == 0:
                i += 1
            else:
                j = lps[j]
            if j == m:
                return i - m  # return starting index of matched pattern
        return -1

    @staticmethod
    def construct_longest_prefix_suffix(p: str, m: int) -> list:
        lps = [0] * (m + 1)
        length, i = 0, 1
        while i < m:
            if p[i] == p[length]:
                length += 1
                i += 1  # lps shifting index by 1, update index first
                lps[i] = length
            elif length == 0:
                i += 1
            else:
                # get the maximum length of last matched letter
                length = lps[length]
        return lps
