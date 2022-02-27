class Solution:
    def missingNumber2(self, nums) -> int:
        # solution 1 with Gauss' Formula, TC - O(n), SC - O(1)
        nums_sum = sum(nums)
        n = len(nums)
        n_sum = n * (n + 1) // 2
        return n_sum - nums_sum

    def missingNumber(self, nums) -> int:
        # solution 1 with Cyclic Sort, TC - O(n), SC - O(1)
        i, n = 0, len(nums)
        while i < n:
            if nums[i] < n and i != nums[i]:
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
            else:
                i += 1

        for i in range(n):
            if nums[i] != i:
                return i

        return len(nums)


if __name__ == '__main__':
    solution = Solution()
    my_nums = [3, 0, 1]
    result = solution.missingNumber2(my_nums)
    print(result)
    result = solution.missingNumber(my_nums)
    print(result)
