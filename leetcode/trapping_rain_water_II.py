import heapq


class Solution(object):
    def trapRainWater(self, heights: list) -> int:
        if not heights or not heights[0]:
            return 0

        n, m = len(heights), len(heights[0])
        heap = []
        visited = [[False for col in range(m)] for row in range(n)]

        for col in range(m):
            heapq.heappush(heap, (heights[0][col], 0, col))
            visited[0][col] = True
            heapq.heappush(heap, (heights[-1][col], n - 1, col))
            visited[n - 1][col] = True

        for row in range(n):
            heapq.heappush(heap, (heights[row][0], row, 0))
            visited[row][0] = True
            heapq.heappush(heap, (heights[row][-1], row, m - 1))
            visited[row][m - 1] = True

        water = 0
        while heap:
            height, row, col = heapq.heappop(heap)
            for row_dir, col_dir in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                new_row, new_col = row + row_dir, col + col_dir
                if 0 <= new_row < n and 0 <= new_col < m and (not
                   visited[new_row][new_col]):
                    water += max(0, height - heights[new_row][new_col])
                    heapq.heappush(heap, (
                        max(height, heights[new_row][new_col]), new_row,
                        new_col))
                    visited[new_row][new_col] = True

        return water
