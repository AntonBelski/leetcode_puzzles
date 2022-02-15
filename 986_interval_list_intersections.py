from typing import List


class Solution:
    def intervalIntersection(self, fl: List[List[int]], sl: List[List[int]]) -> List[List[int]]:
        results = []
        i, j = 0, 0

        while i < len(fl) and j < len(sl):
            lo = max(fl[i][0], sl[j][0])
            hi = min(fl[i][1], sl[j][1])

            if lo <= hi:
                results.append([lo, hi])

            if fl[i][1] < sl[j][1]:
                i += 1
            else:
                j += 1

        return results


if __name__ == '__main__':
    solution = Solution()
    firstList = [[0, 2], [5, 10], [13, 23], [24, 25]]
    secondList = [[1, 5], [8, 12], [15, 24], [25, 26]]
    res = solution.intervalIntersection(firstList, secondList)
    print(res)
