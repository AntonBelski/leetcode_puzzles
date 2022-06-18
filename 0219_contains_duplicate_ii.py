from collections import defaultdict
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        history = defaultdict(int)
        for i, val in enumerate(nums):
            if val in history:
                if i - history[val] <= k:
                    return True
            history[val] = i
        return False


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 2, 3, 1, 2, 3]
    k = 2
    result = solution.containsNearbyDuplicate(nums, k)
    print(result)
