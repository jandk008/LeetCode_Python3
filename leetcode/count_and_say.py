class Solution(object):
    def count_and_say(self, n: int) -> str:
        return self._helper(1, n, '1')

    def _helper(self, _: int, n: int, prefix: str) -> str:
        if _ is n:
            return prefix
        count, char, new_prefix = 1, prefix[0], ''
        for i in range(1, len(prefix)):
            if prefix[i] == char:
                count += 1
            else:
                new_prefix += str(count) + char
                count, char = 1, prefix[i]
        return self._helper(_ + 1, n, new_prefix + str(count) + char)
