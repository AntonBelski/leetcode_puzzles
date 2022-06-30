from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.rows = len(heights)
        self.cols = len(heights[0])
        self.rain = [[0] * self.cols for _ in range(self.rows)]
        self.result = []

        def dfs(heights, r, c, ocean, prev_size=0):
            if not (0 <= r < self.rows and 0 <= c < self.cols):
                return
            if self.rain[r][c] >= ocean or heights[r][c] < prev_size:
                return

            self.rain[r][c] += ocean
            if self.rain[r][c] == 3:
                self.result.append([r, c])

            for _r, _c in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                dfs(heights, r + _r, c + _c, ocean, heights[r][c])

        for _r, _c, ocean in [[0, 0, 1], [self.rows - 1, self.cols - 1, 2]]:
            for r in range(self.rows):
                dfs(heights, r, _c, ocean)
            for c in range(self.cols):
                dfs(heights, _r, c, ocean)

        return self.result


if __name__ == '__main__':
    solution = Solution()
    heights = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
    result = solution.pacificAtlantic(heights)
    print(result)
