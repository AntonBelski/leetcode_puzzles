from typing import List


class Solution:
    def search2(self, nums: List[int], target: int) -> int:
        # Recursive solution, TC - O(log(n))
        lo = 0
        hi = len(nums) - 1

        while lo <= hi:
            if nums[lo] == target:
                return lo

            mid = (lo + hi) // 2
            if target < nums[mid]:
                hi = mid - 1
            elif target > nums[mid]:
                lo = mid + 1
            else:
                return mid

        return -1

    def search(self, nums, target, lo=None, hi=None):
        # Iterative solution, TC - O(log(n))
        if lo is None:
            lo = 0
            hi = len(nums) - 1

        if lo > hi:
            return -1

        if nums[lo] == target:
            return lo

        mid = (lo + hi) // 2
        if target < nums[mid]:
            return self.search(nums, target, lo, mid - 1)
        elif target > nums[mid]:
            return self.search(nums, target, mid + 1, hi)
        else:
            return mid


if __name__ == '__main__':
    solution = Solution()
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    result = solution.search(nums, target)
    print(result)
    result = solution.search2(nums, target)
    print(result)
