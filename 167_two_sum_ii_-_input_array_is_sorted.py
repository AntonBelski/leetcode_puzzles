class Solution:
    def twoSum(self, nums, target):
        left = 0
        right = len(nums) - 1

        while nums[left] + nums[right] != target:
            if nums[left] + nums[right] > target:
                right -= 1
            if nums[left] + nums[right] < target:
                left += 1

        return [left + 1, right + 1]


if __name__ == '__main__':
    solution = Solution()
    numbers = [2, 7, 11, 15]
    target = 9
    res = solution.twoSum(numbers, target)
    print(res)
