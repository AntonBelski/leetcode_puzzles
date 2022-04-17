from typing import List
from heapq import heapify, heappop, heappush


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        max_heap, min_heap = [], []
        max_capital = w

        for i in range(len(profits)):
            min_heap.append([capital[i], profits[i]])

        heapify(min_heap)
        for _ in range(k):
            while min_heap and min_heap[0][0] <= max_capital:
                heappush(max_heap, -heappop(min_heap)[1])

            if not max_heap:
                break

            max_capital += -heappop(max_heap)

        return max_capital


if __name__ == '__main__':
    solution = Solution()
    k = 2
    w = 0
    profits = [1, 2, 3]
    capital = [0, 1, 1]
    result = solution.findMaximizedCapital(k, w, profits, capital)
    print(result)
