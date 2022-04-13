from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        deq = deque()

        for i in range(k):
            while deq and nums[i] > deq[-1]:
                deq.pop()
            deq.append(nums[i])

        result.append(deq[0])

        for i in range(k, len(nums)):
            if deq[0] == nums[i - k]:
                deq.popleft()

            while deq and nums[i] > deq[-1]:
                deq.pop()
            deq.append(nums[i])
            result.append(deq[0])

        return result


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    result = solution.maxSlidingWindow(nums, k)
    print(result)
