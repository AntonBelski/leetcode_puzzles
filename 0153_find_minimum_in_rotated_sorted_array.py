from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo != hi:
            mid = (lo + hi) // 2
            if nums[lo] < nums[hi] or nums[lo] > nums[mid]:
                hi = mid
            else:
                lo = mid + 1
        return nums[lo]


if __name__ == '__main__':
    solution = Solution()
    nums = [3, 4, 5, 1, 2]
    result = solution.findMin(nums)
    print(result)
