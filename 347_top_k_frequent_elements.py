from typing import List
from collections import Counter
from heapq import heappush, heappop


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_freq = Counter(nums)
        result = []

        for num, freq in nums_freq.items():
            heappush(result, (freq, num))
            if len(result) > k:
                heappop(result)

        for i in range(len(result)):
            result[i] = result[i][1]

        return result


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    result = solution.topKFrequent(nums, k)
    print(result)
