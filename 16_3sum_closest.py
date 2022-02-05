from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = float('inf')

        for i in range(len(nums) - 2):
            curr_closest = self.twoSum(nums[i], nums[i + 1:], target)
            if abs(target - curr_closest) < abs(target - closest):
                closest = curr_closest

        return closest

    def twoSum(self, first, curr_nums, target):
        l = 0
        r = len(curr_nums) - 1
        curr_closest = float('inf')

        while r > l:
            curr_sum = first + curr_nums[l] + curr_nums[r]
            if abs(target - curr_sum) < abs(target - curr_closest):
                curr_closest = curr_sum

            if curr_sum > target:
                r -= 1
            else:
                l += 1

        return curr_closest


if __name__ == '__main__':
    solution = Solution()
    nums = [-1, 2, 1, -4]
    target = 1
    res = solution.threeSumClosest(nums, target)
    print(res)
