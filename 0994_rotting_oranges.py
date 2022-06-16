from collections import deque
from typing import List


class Solution:
    def generate_all_pairs(self, row, col, rows, cols, grid):
        pairs = []
        if row - 1 >= 0 and grid[row - 1][col] == 1:
            pairs.append([row - 1, col])
        if row + 1 < rows and grid[row + 1][col] == 1:
            pairs.append([row + 1, col])
        if col - 1 >= 0 and grid[row][col - 1] == 1:
            pairs.append([row, col - 1])
        if col + 1 < cols and grid[row][col + 1] == 1:
            pairs.append([row, col + 1])
        return pairs

    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh_count, mn = 0, 0
        deq = deque()
        all_pairs = []
        rows, cols = len(grid), len(grid[0])

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    deq.append([row, col, 0])
                elif grid[row][col] == 1:
                    fresh_count += 1

        while deq:
            row, col, mn = deq.popleft()
            pairs = self.generate_all_pairs(row, col, rows, cols, grid)
            for r, c in pairs:
                fresh_count -= 1
                deq.append([r, c, mn + 1])
                grid[r][c] = 2

        if fresh_count == 0:
            return mn
        else:
            return -1


if __name__ == '__main__':
    solution = Solution()
    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    result = solution.orangesRotting(grid)
    print(result)
