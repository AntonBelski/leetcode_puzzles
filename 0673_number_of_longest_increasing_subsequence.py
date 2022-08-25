from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        lis_count = 0
        max_size = 1

        for i, num in enumerate(nums):
            if max_size == 1:
                lis_count += 1
            for prev_i in range(i):
                if nums[prev_i] < num:
                    dp[i] = max(dp[i], dp[prev_i] + 1)
                    if dp[i] == max_size:
                        lis_count += 1
                    else:
                        max_size = dp[i]
                        lis_count = 1

        return lis_count


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 3, 5, 4, 7]
    result = solution.findNumberOfLIS(nums)
    print(result)
