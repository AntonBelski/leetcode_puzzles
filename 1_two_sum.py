class Solution:
    def twoSum(self, nums, target):
        nums_dict = {}
        for ind, elem in enumerate(nums):
            nums_dict[elem] = ind
        n = len(nums)
        for i in range(0, n-1):
            sum_part = nums[i] - target
            if nums_dict.get(sum_part) and nums_dict[sum_part] != i:
                return [i, nums_dict[sum_part]]


if __name__ == '__main__':
    solution = Solution()
    result = solution.twoSum([2, 7, 11, 15], 9)
    print(result)
