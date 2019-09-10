from collections import deque


class Solution(object):
    def ladder_length(self, begin_word, end_word, word_list):
        if end_word not in word_list:
            return 0
        length = len(begin_word)
        queue = deque()
        queue.append((begin_word, 1))
        visited = {begin_word: True}
        while queue:
            current, level = queue.popleft()
            for i in range(length):
                for replace in range(97, 122):
                    next_word = current[:i] + chr(replace) + current[i + 1:]
                    if next_word in word_list and next_word not in visited:
                        if next_word == end_word:
                            return level + 1
                        visited[next_word] = True
                        queue.append((next_word, level + 1))
        return 0
