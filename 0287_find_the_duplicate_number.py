from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]):
        n = len(nums)

        for i in range(n):
            while nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        for i in range(n):
            if i + 1 != nums[i]:
                return nums[i]


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 3, 4, 2, 2]
    result = solution.findDuplicate(nums)
    print(result)
