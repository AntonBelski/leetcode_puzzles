from typing import List


class Solution:
    # solution 1 with sorting, complexity - O(n^2)
    def twoSum(self, first, curr_num, result):
        l = 0
        r = len(curr_num) - 1

        while r > l:
            if first + curr_num[l] + curr_num[r] > 0:
                r -= 1
            elif first + curr_num[l] + curr_num[r] < 0:
                l += 1
            else:
                result.add((first, curr_num[l], curr_num[r]))
                l += 1

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        nums.sort()
        result = set()

        for i in range(len(nums) - 2):
            self.twoSum(first=nums[i], curr_num=nums[i + 1:], result=result)

        return [list(s) for s in result]


if __name__ == '__main__':
    solution = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    res = solution.threeSum(nums)
    print(res)
