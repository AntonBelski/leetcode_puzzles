from typing import List
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict


class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end


class Solution:
    def employeeFreeTime2(self, schedules: '[[Interval]]') -> '[Interval]':
        # My Solution, Time Complexity - O(N*log(k)), Space Complexity - O(N)
        result = []
        free_times = []

        for schedule in schedules:
            free_time = []
            start = -float('inf')
            for work_time in schedule:
                free_time.append([start, work_time.start])
                start = work_time.end
            free_time.append([start, float('inf')])
            free_times.append(free_time)

        curr_time_heap = []
        heap = [[e[0][0], e[0][1], i, 0] for i, e in enumerate(free_times)]
        heapify(heap)

        while heap:
            start, end, emp_i, i = heappop(heap)
            if i + 1 < len(free_times[emp_i]):
                new_start = free_times[emp_i][i + 1][0]
                new_end = free_times[emp_i][i + 1][1]
                new_val = [new_start, new_end, emp_i, i + 1]
                heappush(heap, new_val)

            heappush(curr_time_heap, end)
            while curr_time_heap and curr_time_heap[0] <= start:
                heappop(curr_time_heap)

            if len(curr_time_heap) == len(free_times):
                result.append(Interval(start, curr_time_heap[0]))

        return result[1:-1]

    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        # Smarter Solution, Time Complexity - O(N*log(k)), Space Complexity - O(k)
        result = []
        heap = [[e[0].start, e[0].end, i, 0] for i, e in enumerate(schedule)]
        heapify(heap)
        prev_end = heap[0][1]

        while heap:
            start, end, emp_i, i = heappop(heap)
            if i + 1 < len(schedule[emp_i]):
                next_start = schedule[emp_i][i + 1].start
                next_end = schedule[emp_i][i + 1].end
                next_event = [next_start, next_end, emp_i, i + 1]
                heappush(heap, next_event)

            if start > prev_end:
                result.append(Interval(prev_end, start))
            prev_end = max(prev_end, end)

        return result


if __name__ == '__main__':
    solution = Solution()
    empl1_event1 = Interval(1, 2)
    empl1_event2 = Interval(5, 6)
    empl2_event1 = Interval(1, 3)
    empl3_event1 = Interval(4, 10)
    schedule = [[empl1_event1, empl1_event2], [empl2_event1], [empl3_event1]]
    result = solution.employeeFreeTime(schedule=schedule)
    print('Solution 1:')
    for i, interval in enumerate(result):
        print(f'Interval {i + 1}: start={interval.start}, end={interval.end}')
    print()

    result2 = solution.employeeFreeTime(schedule=schedule)
    print('Solution 2:')
    for i, interval in enumerate(result2):
        print(f'Interval {i + 1}: start={interval.start}, end={interval.end}')
