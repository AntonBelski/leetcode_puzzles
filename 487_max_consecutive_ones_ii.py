from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        is_zero_checked = False
        max_len = 0
        start = 0

        for end in range(len(nums)):
            if nums[end] == 0:
                if not is_zero_checked:
                    is_zero_checked = True
                else:
                    while nums[start] != 0:
                        start += 1
                    start += 1

            max_len = max(max_len, end + 1 - start)

        return max_len


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 0, 1, 1, 0]
    res = solution.findMaxConsecutiveOnes(nums)
    print(res)
