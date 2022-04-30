from typing import List


class Solution:
    def binary_search(self, arr, x):
        lo, hi = 0, len(arr)
        while lo != hi:
            mid = (lo + hi) // 2
            if x <= arr[mid]:
                hi = mid
            else:
                lo = mid + 1
        return lo

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = self.binary_search(nums, target)
        end = self.binary_search(nums, target + 1) - 1

        if start < len(nums) and nums[start] == target:
            return [start, end]
        else:
            return [-1, -1]


if __name__ == '__main__':
    solution = Solution()
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    result = solution.searchRange(nums, target)
    print(result)
