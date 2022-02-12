from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        results = []
        intervals.sort(key=lambda k: k[0])

        start = intervals[0][0]
        end = intervals[0][1]

        for curr_start, curr_end in intervals[1:]:
            if curr_start > end:
                results.append([start, end])
                start = curr_start
                end = curr_end
            else:
                end = max(end, curr_end)

        results.append([start, end])

        return results


if __name__ == '__main__':
    solution = Solution()
    nums = [[1, 3], [2, 6], [8, 10], [15, 18]]
    res = solution.merge(nums)
    print(res)
