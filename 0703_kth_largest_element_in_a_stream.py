from heapq import heappush, heappushpop, heappop
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        for elem in nums:
            if len(self.heap) < k:
                heappush(self.heap, elem)
            else:
                heappushpop(self.heap, elem)

    def add(self, val: int) -> int:
        heappush(self.heap, val)
        if len(self.heap) > self.k:
            heappop(self.heap)
        return self.heap[0]


if __name__ == '__main__':
    kth_largest = KthLargest(3, [4, 5, 8, 2])
    print(kth_largest.add(3))
    print(kth_largest.add(5))
    print(kth_largest.add(10))
    print(kth_largest.add(9))
    print(kth_largest.add(4))
