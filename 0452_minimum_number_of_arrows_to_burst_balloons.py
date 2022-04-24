from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        pairs = sorted(points, key=lambda x: x[0])
        next_shot = pairs[0]
        result = 0

        for pair in pairs:
            if next_shot[1] < pair[0]:
                result += 1
                next_shot = pair
            else:
                next_shot = [pair[0], min(pair[1], next_shot[1])]

        return result + 1


if __name__ == '__main__':
    solution = Solution()
    points = [[10, 16], [2, 8], [1, 6], [7, 12]]
    result = solution.findMinArrowShots(points)
    print(result)
