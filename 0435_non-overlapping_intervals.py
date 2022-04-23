from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        pairs = sorted(intervals, key=lambda x: x[0])
        first = pairs[0]
        result = 0

        for second in pairs[1:]:
            if second[0] < min(first[1], second[1]):
                if first[1] > second[1]:
                    first = second
                result += 1
            else:
                first = second

        return result


if __name__ == '__main__':
    solution = Solution()
    intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
    result = solution.eraseOverlapIntervals(intervals)
    print(result)
