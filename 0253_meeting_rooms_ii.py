from heapq import heapify, heappop
from typing import List


class Solution:
    def minMeetingRooms2(self, intervals: List[List[int]]) -> int:
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

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        max_rooms, rooms = 0, 0
        start_heap = [pair[0] for pair in intervals]
        end_heap = [pair[1] for pair in intervals]

        heapify(start_heap)
        heapify(end_heap)
        while start_heap:
            time = heappop(start_heap)
            rooms += 1
            while end_heap[0] <= time:
                heappop(end_heap)
                rooms -= 1
            max_rooms = max(rooms, max_rooms)

        return max_rooms


if __name__ == '__main__':
    solution = Solution()
    intervals = [[0, 30], [5, 10], [15, 20]]
    res = solution.minMeetingRooms2(intervals)
    print(res)
    res = solution.minMeetingRooms(intervals)
    print(res)
