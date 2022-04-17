from typing import List
from heapq import heapify, heappop


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        start_heap, end_heap = [], []

        for i, pair in enumerate(intervals):
            start_heap.append([pair[0], i])
            end_heap.append([pair[1], i])

        heapify(start_heap)
        heapify(end_heap)

        results = [-1] * len(intervals)

        while end_heap:
            end, end_ind = heappop(end_heap)

            while start_heap and start_heap[0][0] < end:
                heappop(start_heap)

            if start_heap:
                results[end_ind] = start_heap[0][1]

        return results


if __name__ == '__main__':
    solution = Solution()
    intervals = [[3, 4], [2, 3], [1, 2]]
    result = solution.findRightInterval(intervals)
    print(result)
