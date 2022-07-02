from typing import List


class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        h_cuts = sorted(horizontalCuts)
        w_cuts = sorted(verticalCuts)

        h_max = max(h_cuts[0], h - h_cuts[-1])
        w_max = max(w_cuts[0], w - w_cuts[-1])

        for i in range(1, len(h_cuts)):
            h_max = max(h_max, h_cuts[i] - h_cuts[i - 1])
        for i in range(1, len(w_cuts)):
            w_max = max(w_max, w_cuts[i] - w_cuts[i - 1])

        return (h_max * w_max) % (10 ** 9 + 7)


if __name__ == '__main__':
    solution = Solution()
    h = 5
    w = 4
    horizontalCuts = [1, 2, 4]
    verticalCuts = [1, 3]
    result = solution.maxArea(h, w, horizontalCuts, verticalCuts)
    print(result)
