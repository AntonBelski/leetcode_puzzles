from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        odd_last = 0

        for i in range(len(nums)):
            if nums[i] % 2 == 0 and i != odd_last:
                nums[i], nums[odd_last] = nums[odd_last], nums[i]
            if nums[odd_last] % 2 == 0:
                odd_last += 1

        return nums


if __name__ == '__main__':
    solution = Solution()
    nums = [3, 1, 2, 4]
    result = solution.sortArrayByParity(nums)
    print(result)
