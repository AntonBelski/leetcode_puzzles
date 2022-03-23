from typing import List


class Solution:
    def trap(self, heights: List[int]) -> int:
        result = 0
        n = len(heights)
        max_ind = 0

        for i, h in enumerate(heights):
            if h >= heights[max_ind]:
                max_ind = i

        curr_max = 0
        for i in range(max_ind):
            if heights[i] > curr_max:
                curr_max = heights[i]
            else:
                result += curr_max - heights[i]

        curr_max = 0
        for i in range(n - 1, max_ind, -1):
            if heights[i] > curr_max:
                curr_max = heights[i]
            else:
                result += curr_max - heights[i]

        return result


if __name__ == '__main__':
    solution = Solution()
    heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    result = solution.trap(heights)
    print(result)
