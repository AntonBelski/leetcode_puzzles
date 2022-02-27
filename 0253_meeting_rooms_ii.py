from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        rooms = 0
        s, e = 0, 0

        start_times = sorted([i[0] for i in intervals])
        end_times = sorted([i[1] for i in intervals])

        while s < len(intervals) and e < len(intervals):
            if start_times[s] < end_times[e]:
                s += 1
                rooms += 1
            else:
                s += 1
                e += 1

        return rooms


if __name__ == '__main__':
    solution = Solution()
    intervals = [[0, 30], [5, 10], [15, 20]]
    res = solution.minMeetingRooms(intervals)
    print(res)
