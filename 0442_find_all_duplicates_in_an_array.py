from typing import List


class Solution:
    def findDuplicates2(self, nums: List[int]) -> List[int]:
        # solution 1 with negative integers, TC - O(n), SC - O(1)
        results = []

        for i in range(len(nums)):
            elem = abs(nums[i]) - 1
            if nums[elem] < 0:
                results.append(elem + 1)
            else:
                nums[elem] *= -1

        return results

    def findDuplicates(self, nums: List[int]) -> List[int]:
        # solution 1 with Cyclic Sort, TC - O(n), SC - O(1)
        n = len(nums)
        results = []

        for i in range(n):
            while nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        for i in range(n):
            if i + 1 != nums[i]:
                results.append(nums[i])

        return results


if __name__ == '__main__':
    solution = Solution()
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    result = solution.findDuplicates2(nums.copy())
    print(result)
    result = solution.findDuplicates(nums.copy())
    print(result)
