class Solution:
    def findDisappearedNumbers2(self, nums):
        # solution 1 with negative integers, TC - O(n), SC - O(1)
        n = len(nums)
        for i in range(n):
            elem = abs(nums[i]) - 1
            if nums[elem] > 0:
                nums[elem] *= -1
        results = []
        for i in range(n):
            if nums[i] > 0:
                results.append(i + 1)
        return results

    def findDisappearedNumbers(self, nums):
        # solution 1 with Cyclic Sort, TC - O(n), SC - O(1)
        n = len(nums)
        result = []

        for i in range(n):
            while nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        for i in range(n):
            if i + 1 != nums[i]:
                result.append(i + 1)

        return result


if __name__ == '__main__':
    solution = Solution()
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    result = solution.findDisappearedNumbers2(nums.copy())
    print(result)
    result = solution.findDisappearedNumbers(nums.copy())
    print(result)
