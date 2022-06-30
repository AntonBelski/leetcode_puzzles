from collections import deque
from typing import List


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        deq = deque()
        n = len(grid)

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    deq.append([r, c, 1])

        while deq:
            r, c, dist = deq.popleft()
            if not (0 <= r < n and 0 <= c < n) or grid[r][c] not in [0, 1]:
                continue
            elif grid[r][c] == 1:
                grid[r][c] = -1
            else:
                grid[r][c] = dist

            for new_r, new_c in [[r - 1, c], [r + 1, c], [r, c - 1], [r, c + 1]]:
                deq.append([new_r, new_c, dist + 1])

        result = -1

        for r in range(n):
            for c in range(n):
                result = max(result, grid[r][c] - 1)

        return result


if __name__ == '__main__':
    solution = Solution()
    grid = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
    result = solution.maxDistance(grid)
    print(result)
