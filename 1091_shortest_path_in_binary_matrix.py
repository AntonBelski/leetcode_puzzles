from collections import deque
from itertools import product
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        matrix = []

        if grid[0][0] + grid[-1][-1] != 0:
            return -1

        for r in range(len(grid)):
            matrix.append([])
            for c in range(len(grid[0])):
                matrix[r].append(-grid[r][c])

        deq = deque()
        deq.append([0, 0, 1])

        while deq:
            r, c, curr_path = deq.popleft()
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0])):
                continue
            elif matrix[r][c] != 0 and curr_path >= matrix[r][c]:
                continue

            matrix[r][c] = curr_path
            for _r, _c in product([-1, 0, 1], repeat=2):
                if _r != 0 or _c != 0:
                    deq.append([r + _r, c + _c, curr_path + 1])

        if matrix[-1][-1] != 0:
            return matrix[-1][-1]
        else:
            return -1


if __name__ == '__main__':
    solution = Solution()
    grid = [[0, 1, 1, 0, 0, 0], [0, 1, 0, 1, 1, 0], [0, 1, 1, 0, 1, 0], [0, 0, 0, 1, 1, 0], [1, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 0]]
    result = solution.shortestPathBinaryMatrix(grid)
    print(result)
