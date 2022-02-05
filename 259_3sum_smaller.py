from typing import List


class Solution:
    def twoSum(self, first, curr_num, target):
        l = 0
        r = len(curr_num) - 1
        result = 0

        while r > l:
            curr_sum = first + curr_num[r] + curr_num[l]
            if curr_sum < target:
                result += r - l
                l += 1
            else:
                r -= 1

        return result

    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        result = 0
        nums.sort()

        for i in range(len(nums) - 2):
            result += self.twoSum(nums[i], nums[i + 1:], target)

        return result


if __name__ == '__main__':
    solution = Solution()
    nums = [-2, 0, 1, 3]
    target = 2
    res = solution.threeSumSmaller(nums, target)
    print(res)
