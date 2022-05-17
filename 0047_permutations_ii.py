from typing import List


class Solution:
    # Time Complexity - O(Σ(k * P(N, k))), Space Complexity - O(n^2), description of asymptotic in the notebook.
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result, current = [], []
        self.nums_len = len(nums)
        self.backtracking(nums, result, current)
        return result

    def backtracking(self, nums, result, current):
        if len(current) == self.nums_len:
            result.append(current[:])
            return
        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            current.append(nums[i])
            new_nums = nums[:i] + nums[i + 1:]
            self.backtracking(new_nums, result, current)
            current.pop()


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 1, 2]
    result = solution.permuteUnique(nums)
    print(result)
