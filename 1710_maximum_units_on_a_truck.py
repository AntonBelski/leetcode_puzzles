from heapq import heapify, heappop
from typing import List


class Solution:
    def maximumUnits2(self, box_types: List[List[int]], truck_size: int) -> int:
        # Heap, Time Complexity - O(n * logn), Space Complexity - O(n)
        heap = [[-val, size] for size, val in box_types]
        heapify(heap)
        rest = truck_size
        result = 0

        while heap and rest != 0:
            boxes, size = heappop(heap)
            count = min(size, rest)
            result += -boxes * count
            rest -= count

        return result

    def maximumUnits(self, box_types: List[List[int]], truck_size: int) -> int:
        # Counting Sort, Time Complexity - O(n), Space Complexity - O(1)
        boxes = [0] * 1001
        rest = truck_size
        result = 0

        for amount, box_size in box_types:
            boxes[box_size] += amount

        for box_size in range(1000, -1, -1):
            amount = min(rest, boxes[box_size])
            rest -= amount
            result += amount * box_size

            if rest == 0:
                break

        return result


if __name__ == '__main__':
    solution = Solution()
    boxTypes = [[1, 3], [2, 2], [3, 1]]
    truckSize = 4
    result = solution.maximumUnits2(boxTypes, truckSize)
    print(result)
    result = solution.maximumUnits(boxTypes, truckSize)
    print(result)
