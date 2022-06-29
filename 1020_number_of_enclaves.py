from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def dfs(grid, r, c):
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0])):
                return -float('inf')
            elif grid[r][c] != 1:
                return 0

            grid[r][c] = 0
            return 1 + sum([dfs(grid, r - 1, c), dfs(grid, r + 1, c),
                            dfs(grid, r, c - 1), dfs(grid, r, c + 1)])

        result = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                result += max(0, dfs(grid, r, c))

        return result


if __name__ == '__main__':
    solution = Solution()
    grid = [[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
    result = solution.numEnclaves(grid)
    print(result)
