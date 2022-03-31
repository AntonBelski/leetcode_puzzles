from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        result = []

        for elem in nums:
            heapq.heappush(result, elem)
            if len(result) > k:
                heapq.heappop(result)

        return result[0]

        # or 'return heapq.nlargest(result, k)[-1]'


if __name__ == '__main__':
    solution = Solution()
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    result = solution.findKthLargest(nums, k)
    print(result)
