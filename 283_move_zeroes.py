from typing import List


class Solution:
    # first solution, TC - O(n), SP - O(1)
    def move_zeroes1(self, nums: List[int]) -> None:
        zero_i = 0
        not_zero_i = 0
        n = len(nums)

        while not_zero_i < n and nums[not_zero_i] == 0:
            not_zero_i += 1
        while zero_i < n and nums[zero_i] != 0 and zero_i < not_zero_i:
            zero_i += 1

        while not_zero_i < n and zero_i < n:
            nums[not_zero_i], nums[zero_i] = nums[zero_i], nums[not_zero_i]
            zero_i += 1
            not_zero_i += 1

            while not_zero_i < n and nums[not_zero_i] == 0:
                not_zero_i += 1
            while zero_i < n and nums[zero_i] != 0 and zero_i < not_zero_i:
                zero_i += 1

    # first solution, TC - O(n), SP - O(1)
    def move_zeroes2(self, nums: List[int]) -> None:
        not_zero_i = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                if i != not_zero_i:
                    nums[not_zero_i], nums[i] = nums[i], nums[not_zero_i]
                not_zero_i += 1


if __name__ == '__main__':
    solution = Solution()
    nums = [0, 1, 0, 3, 12]
    solution.move_zeroes1(nums)
    print(nums)
    nums = [0, 1, 0, 3, 12]
    solution.move_zeroes2(nums)
    print(nums)
