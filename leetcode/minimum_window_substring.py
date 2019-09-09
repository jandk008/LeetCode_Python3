from collections import Counter


class Solution(object):
    def min_window(self, s: str, t: str) -> str:
        count = Counter(t)
        missing = len(t)
        start = 0
        res = ""
        for end in range(len(s)):
            if s[end] in t:
                if count[s[end]] > 0:
                    missing -= 1
                count[s[end]] -= 1
            if missing == 0:
                while s[start] not in t or count[s[start]] < 0:
                    if s[start] in count:
                        count[s[start]] += 1
                    start += 1
                res = s[start: end + 1] if not res or (
                    end - start < len(res)) else res
                count[s[start]] += 1
                missing += 1
                start += 1
        return res
