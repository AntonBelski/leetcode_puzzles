from typing import List


class Solution:
    def twoSum(self, first, second, curr_nums, target, result):
        l = 0
        r = len(curr_nums) - 1

        while r > l:
            curr_sum = first + second + curr_nums[r] + curr_nums[l]
            if curr_sum > target:
                r -= 1
            elif curr_sum < target:
                l += 1
            else:
                result.add((first, second, curr_nums[l], curr_nums[r]))
                l += 1

    def fourSum(self, nums: List[int], target: int):
        if len(nums) < 4:
            return []

        nums.sort()
        result = set()

        for start in range(len(nums) - 3):
            for second in range(start + 1, len(nums) - 2):
                self.twoSum(nums[start], nums[second], nums[second + 1:], target, result)

        return result


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    res = solution.fourSum(nums, target)
    print(res)
