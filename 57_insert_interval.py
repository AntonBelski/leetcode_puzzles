from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        results = []
        i = 0
        start, end = 0, 1
        n = len(intervals)

        while i < n and intervals[i][end] < newInterval[start]:
            results.append(intervals[i])
            i += 1

        while i < n and intervals[i][start] <= newInterval[end]:
            newInterval[start] = min(newInterval[start], intervals[i][start])
            newInterval[end] = max(newInterval[end], intervals[i][end])
            i += 1

        results.append(newInterval)

        while i < n:
            results.append(intervals[i])
            i += 1

        return results


if __name__ == '__main__':
    solution = Solution()
    intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    newInterval = [4, 8]
    res = solution.insert(intervals, newInterval)
    print(res)
