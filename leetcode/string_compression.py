
class Solution(object):
    def compress(self, chars: list) -> int:
        if not chars or len(chars) == 1:
            return len(chars)
        insert_index, start, end = 0, 0, 0
        while end < len(chars):
            end += 1
            while end < len(chars) and chars[start] == chars[end]:
                end += 1
            chars[insert_index] = chars[start]
            insert_index += 1
            if end - start > 1:
                count = list(str(end - start))
                chars[insert_index: insert_index + len(count)] = count
                insert_index += len(count)
            start = end
        del chars[insert_index:]
        return len(chars)
