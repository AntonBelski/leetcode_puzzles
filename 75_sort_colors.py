from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        last_not_zero = 0
        last_not_two = len(nums) - 1
        i = 0

        while i <= last_not_two:
            if nums[i] == 2:
                nums[i], nums[last_not_two] = nums[last_not_two], nums[i]
                last_not_two -= 1
            elif nums[i] == 0:
                nums[i], nums[last_not_zero] = nums[last_not_zero], nums[i]
                last_not_zero += 1
                i += 1
            else:
                i += 1


if __name__ == '__main__':
    solution = Solution()
    nums = [2, 0, 2, 1, 1, 0]
    solution.sortColors(nums)
    print(nums)
