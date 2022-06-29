from typing import List


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def dfs(grid1, grid2, r, c):
            if not (0 <= r < len(grid2) and 0 <= c < len(grid2[0])):
                return True
            elif grid2[r][c] == 0:
                return True
            elif grid1[r][c] == 0:
                return False

            grid2[r][c] = 0
            return all([dfs(grid1, grid2, r - 1, c),
                        dfs(grid1, grid2, r + 1, c),
                        dfs(grid1, grid2, r, c - 1),
                        dfs(grid1, grid2, r, c + 1)])

        result = 0

        for r in range(len(grid2)):
            for c in range(len(grid2[0])):
                if grid2[r][c] == 1 and dfs(grid1, grid2, r, c):
                    result += 1

        return result


if __name__ == '__main__':
    solution = Solution()
    grid1 = [[1, 1, 1, 0, 0], [0, 1, 1, 1, 1], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 0, 1, 1]]
    grid2 = [[1, 1, 1, 0, 0], [0, 0, 1, 1, 1], [0, 1, 0, 0, 0], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]]
    result = solution.countSubIslands(grid1, grid2)
    print(result)
