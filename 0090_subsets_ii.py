from typing import List


class Solution:
    def recursive_subsets(self, nums, index=0):
        for i in range(index, len(nums)):
            self.subset.append(nums[i])
            subset_tuple = tuple(self.subset)
            if subset_tuple not in self.subsets:
                self.result.append(self.subset[:])
                self.subsets.add(subset_tuple)
            self.recursive_subsets(nums, i + 1)
            self.subset.pop()

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # My Solution, Time Complexity - O(n * 2^n), Space Complexity - O(n * 2^n)
        nums.sort()
        self.result = [[]]
        self.subset = []
        self.subsets = set()
        self.recursive_subsets(nums)
        return self.result

    def recursive_subsets2(self, nums, result, subset=[], index=0):
        for i in range(index, len(nums)):
            if i != index and nums[i] == nums[i - 1]:
                continue
            subset.append(nums[i])
            result.append(subset[:])
            self.recursive_subsets2(nums, result, subset, i + 1)
            subset.pop()

    def subsetsWithDup2(self, nums: List[int]) -> List[List[int]]:
        # Smart Solution, Time Complexity - O(n * 2^n), Space Complexity - O(n), hard to fully understand
        nums.sort()
        result = [[]]
        self.recursive_subsets2(nums, result)
        return result


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 2, 2]
    result = solution.subsetsWithDup(nums)
    print(result)
    result = solution.subsetsWithDup2(nums)
    print(result)
