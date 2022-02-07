from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        min_l = float('inf')
        min_r = -float('inf')
        is_unsorted_exist = False

        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                is_unsorted_exist = True
                min_l = min(min_l, nums[i])

        if is_unsorted_exist:
            for i in range(len(nums)):
                if nums[i] > min_l:
                    min_l = i
                    break

        for i in (range(len(nums) - 2, -1, -1)):
            if nums[i] > nums[i + 1]:
                is_unsorted_exist = True
                min_r = max(min_r, nums[i])

        if is_unsorted_exist:
            for i in (range(len(nums) - 1, -1, -1)):
                if nums[i] < min_r:
                    min_r = i
                    break

        return min_r + 1 - min_l if is_unsorted_exist else 0


if __name__ == '__main__':
    solution = Solution()
    nums = [2, 6, 4, 8, 10, 9, 15]
    res = solution.findUnsortedSubarray(nums)
    print(res)
