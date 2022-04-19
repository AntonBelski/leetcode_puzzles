from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], new_inter: List[int]) -> List[List[int]]:
        result = []
        start = 0
        n = len(intervals)

        while start < n and intervals[start][1] < new_inter[0]:
            result.append(intervals[start])
            start += 1

        result.append(new_inter)
        while start < n and result[-1][1] >= intervals[start][0]:
            result[-1] = [min(result[-1][0], intervals[start][0]),
                          max(result[-1][1], intervals[start][1])]
            start += 1

        while start < n:
            result.append(intervals[start])
            start += 1

        return result


if __name__ == '__main__':
    solution = Solution()
    intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    newInterval = [4, 8]
    res = solution.insert(intervals, newInterval)
    print(res)
