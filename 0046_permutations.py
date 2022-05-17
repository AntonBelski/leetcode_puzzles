from typing import List


class Solution:
    # Time Complexity - O(n * n!), Space Complexity - O(n), description of asymptotic in the notebook.
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.current = []
        self.backtracking(nums, result)
        return result

    def backtracking(self, nums, result, first=0):
        if len(self.current) == len(nums):
            result.append(self.current[:])
            return
        for i in range(first, len(nums)):
            self.current.append(nums[i])
            nums[i], nums[first] = nums[first], nums[i]
            self.backtracking(nums, result, first + 1)
            nums[i], nums[first] = nums[first], nums[i]
            self.current.pop()


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 2, 3]
    result = solution.permute(nums)
    print(result)
