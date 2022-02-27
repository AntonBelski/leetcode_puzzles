from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            while 0 < nums[i] < n + 1 and nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        for i in range(n):
            if i + 1 != nums[i]:
                return i + 1

        return n + 1


if __name__ == '__main__':
    solution = Solution()
    nums = [3, 4, -1, 1]
    result = solution.firstMissingPositive(nums.copy())
    print(result)
