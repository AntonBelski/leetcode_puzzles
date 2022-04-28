from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)
        while lo != hi:
            mid = (lo + hi) // 2
            if target <= nums[mid]:
                hi = mid
            else:
                lo = mid + 1
        return lo


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 3, 5, 6]
    target = 5
    result = solution.searchInsert(nums, target)
    print(result)
