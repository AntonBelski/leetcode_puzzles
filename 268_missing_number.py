class Solution:
    def missingNumber(self, nums) -> int:
        nums_sum = sum(nums)
        n = len(nums)
        n_sum = n * (n + 1) // 2
        return n_sum - nums_sum


if __name__ == '__main__':
    solution = Solution()
    my_nums = [3, 0, 1]
    result = solution.missingNumber(my_nums)
    print(result)
