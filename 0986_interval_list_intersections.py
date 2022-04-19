from typing import List


class Solution:
    def intervalIntersection(self, fl: List[List[int]], sl: List[List[int]]) -> List[List[int]]:
        result = []
        p1, p2 = 0, 0

        while p1 < len(fl) and p2 < len(sl):
            max_start = max(fl[p1][0], sl[p2][0])
            min_end = min(fl[p1][1], sl[p2][1])

            if min_end >= max_start:
                result.append([max_start, min_end])

            if fl[p1][1] > sl[p2][1]:
                p2 += 1
            else:
                p1 += 1

        return result


if __name__ == '__main__':
    solution = Solution()
    firstList = [[0, 2], [5, 10], [13, 23], [24, 25]]
    secondList = [[1, 5], [8, 12], [15, 24], [25, 26]]
    res = solution.intervalIntersection(firstList, secondList)
    print(res)
