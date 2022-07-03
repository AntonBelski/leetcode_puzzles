from collections import deque
from typing import List


class Solution:
    def find_island_cell(self, grid, rows, cols):
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return r, c

    def shortestBridge(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        matrix = [row[:] for row in grid]

        deq_waves = deque()
        deq_island = deque()
        deq_island.append(self.find_island_cell(grid, rows, cols))

        while deq_island:
            r, c = deq_island.popleft()
            if not (0 <= r < rows and 0 <= c < cols):
                continue
            if matrix[r][c] != 1:
                continue

            matrix[r][c] = 0
            deq_waves.append([r, c, -1])
            for _r, _c in ((0, -1), (0, 1), (1, 0), (-1, 0)):
                deq_island.append([r + _r, c + _c])

        while deq_waves:
            r, c, dist = deq_waves.popleft()
            if not (0 <= r < rows and 0 <= c < cols):
                continue
            if matrix[r][c] == 1:
                return dist
            if matrix[r][c] != 0:
                continue

            matrix[r][c] = -1
            for _r, _c in ((0, -1), (0, 1), (1, 0), (-1, 0)):
                deq_waves.append([r + _r, c + _c, dist + 1])


if __name__ == '__main__':
    solution = Solution()
    grid = [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 1, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]
    result = solution.shortestBridge(grid)
    print(result)
