from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        extra_zero = 0
        start = 0
        end = 0

        while end < len(nums) and nums[end] != 0:
            end += 1

        max_size = end - start

        while end < len(nums):
            if nums[end] == 0:
                if extra_zero == 0:
                    extra_zero = 1
                else:
                    while nums[start] != 0:
                        start += 1
                    start += 1

            max_size = max(max_size, end + 1 - start - extra_zero)
            end += 1

        if extra_zero == 0:
            max_size -= 1

        return max_size


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 1, 0, 1]
    res = solution.longestSubarray(nums)
    print(res)
