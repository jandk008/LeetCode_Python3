class Solution(object):
    def is_subsequence(self, s: str, t: str) -> bool:
        start = -1
        for v in s:
            start = t.find(v, start + 1)
            if start == -1:
                return False
        return True
