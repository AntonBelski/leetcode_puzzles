from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        max_subs = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    max_subs[i] = max(max_subs[i], max_subs[j] + 1)

        return max(max_subs)


if __name__ == '__main__':
    solution = Solution()
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    result = solution.lengthOfLIS(nums)
    print(result)
