from heapq import heappush, heappop
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result = []

        for ind, p in enumerate(points):
            dist = p[0] ** 2 + p[1] ** 2
            heappush(result, (-dist, ind))
            if len(result) > k:
                heappop(result)

        for i in range(len(result)):
            result[i] = points[result[i][1]]

        return result


if __name__ == '__main__':
    solution = Solution()
    points = [[3, 3], [5, -1], [-2, 4]]
    k = 2
    result = solution.kClosest(points, k)
    print(result)
