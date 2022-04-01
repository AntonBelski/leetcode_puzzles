from heapq import heapify, heappush, heappop
from typing import List


class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        result = 0
        heapify(sticks)

        while len(sticks) > 1:
            first_min = heappop(sticks)
            second_min = heappop(sticks)
            result += first_min + second_min
            heappush(sticks, first_min + second_min)

        return result


if __name__ == '__main__':
    solution = Solution()
    sticks = [2, 4, 3]
    result = solution.connectSticks(sticks)
    print(result)
