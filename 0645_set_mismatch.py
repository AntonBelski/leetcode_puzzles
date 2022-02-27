from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for i in range(n):
            while nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        for i in range(n):
            if i + 1 != nums[i]:
                return [nums[i], i + 1]


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 2, 2, 4]
    result = solution.findErrorNums(nums.copy())
    print(result)
