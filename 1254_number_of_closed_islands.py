from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        result = 0

        def dfs(grid, r, c):
            if not 0 <= r < len(grid) or not 0 <= c < len(grid[0]):
                return False
            if grid[r][c] != 0:
                return True

            grid[r][c] = 2
            return all([dfs(grid, r - 1, c),
                        dfs(grid, r + 1, c),
                        dfs(grid, r, c - 1),
                        dfs(grid, r, c + 1)])

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0 and dfs(grid, r, c):
                    result += 1

        return result


if __name__ == '__main__':
    solution = Solution()
    grid = [[1, 1, 1, 1, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 0]]
    result = solution.closedIsland(grid)
    print(result)
