from typing import List


class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        n = len(heights)
        result = [n - 1]

        for i in range(n - 2, -1, -1):
            if heights[i] > heights[result[-1]]:
                result.append(i)

        result.reverse()
        return result


if __name__ == '__main__':
    solution = Solution()
    heights = [4, 2, 3, 1]
    result = solution.findBuildings(heights)
    print(result)
