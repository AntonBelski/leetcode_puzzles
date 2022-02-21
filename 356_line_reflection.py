from typing import List


class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        if len(points) == 0:
            return True

        min_point = min([i[0] for i in points])
        max_point = max([i[0] for i in points])

        points_set = set()
        for p in points:
            points_set.add(tuple(p))

        for p in points:
            if tuple([min_point + max_point - p[0], p[1]]) not in points_set:
                return False

        return True


if __name__ == '__main__':
    solution = Solution()
    points = [[1, 1], [-1, -1]]
    res = solution.isReflected(points)
    print(res)
