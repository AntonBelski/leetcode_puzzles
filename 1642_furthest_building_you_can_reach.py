from typing import List
from heapq import heappop, heappush


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        prev_h = heights[0]
        bricks_jump = 0
        heap = []

        for i, new_h in enumerate(heights[1:]):
            if new_h > prev_h:
                heappush(heap, new_h - prev_h)
                if len(heap) > ladders:
                    bricks_jump += heappop(heap)
                if bricks_jump > bricks:
                    return i
            prev_h = new_h

        return len(heights) - 1


if __name__ == '__main__':
    solution = Solution()
    heights = [4, 12, 2, 7, 3, 18, 20, 3, 19]
    bricks = 10
    ladders = 2
    result = solution.furthestBuilding(heights, bricks, ladders)
    print(result)
