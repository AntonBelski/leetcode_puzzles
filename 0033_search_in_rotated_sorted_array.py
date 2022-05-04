from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo != hi:
            mid = (lo + hi) // 2
            if nums[lo] < nums[hi] or nums[mid + 1] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid
        min_ind = (lo + 1) % len(nums)

        lo, hi = 0, len(nums) - 1
        while lo != hi:
            mid = (lo + hi) // 2
            if target <= nums[(mid + min_ind) % len(nums)]:
                hi = mid
            else:
                lo = mid + 1

        real_lo = (lo + min_ind) % len(nums)
        if nums[real_lo] == target:
            return real_lo
        else:
            return -1


if __name__ == '__main__':
    solution = Solution()
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    result = solution.search(nums, target)
    print(result)
