from typing import List

from heapq import heappop, heappush


class MedianFinder2:
    # My Solution, Space Complexity - O(n)
    # 1 operation - Time Complexity - O(log(n)),
    # n operations - Time Complexity - O(n*log(n)),
    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        if self.max_heap or self.min_heap:
            median = self.findMedian()
            if median <= num:
                heappush(self.min_heap, num)
            else:
                heappush(self.max_heap, -num)
        else:
            heappush(self.max_heap, -num)

        if len(self.max_heap) == len(self.min_heap) + 2:
            val = heappop(self.max_heap)
            heappush(self.min_heap, -val)
        elif len(self.max_heap) + 2 == len(self.min_heap):
            val = heappop(self.min_heap)
            heappush(self.max_heap, -val)

    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        elif len(self.max_heap) < len(self.min_heap):
            return self.min_heap[0]
        else:
            return (-self.max_heap[0] + self.min_heap[0]) / 2


class MedianFinder:
    # Betters Solution, Space Complexity - O(n)
    # 1 operation - Time Complexity - O(log(n)),
    # n operations - Time Complexity - O(n*log(n)),
    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num):
        heappush(self.max_heap, -num)
        heappush(self.min_heap, -heappop(self.max_heap))
        if len(self.min_heap) > len(self.max_heap):
            heappush(self.max_heap, -heappop(self.min_heap))

    def findMedian(self):
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        else:
            return (-self.max_heap[0] + self.min_heap[0]) / 2


if __name__ == '__main__':
    median_finder = MedianFinder()
    median_finder.addNum(1)
    median_finder.addNum(2)
    print(median_finder.findMedian())
    median_finder.addNum(3)
    print(median_finder.findMedian())
    print()
    median_finder = MedianFinder2()
    median_finder.addNum(1)
    median_finder.addNum(2)
    print(median_finder.findMedian())
    median_finder.addNum(3)
    print(median_finder.findMedian())
