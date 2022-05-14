from typing import List


class Solution:
    def recursive_subsets(self, nums, result, start=0):
        for i in range(start, len(nums)):
            self.current_list.append(nums[i])
            result.append(self.current_list[:])
            self.recursive_subsets(nums, result, i + 1)
            self.current_list.pop()
        return result

    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        self.current_list = []
        return self.recursive_subsets(nums, result)


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 2, 3]
    result = solution.subsets(nums)
    print(result)
