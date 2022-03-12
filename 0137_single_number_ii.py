from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        on = 0
        tw = 0

        for n in nums:
            on = ~tw & on & ~n | ~tw & ~on & n
            tw = tw & ~n & ~on | ~tw & n & ~on

        return on


if __name__ == '__main__':
    solution = Solution()
    nums = [0, 1, 0, 1, 0, 1, 99]
    result = solution.singleNumber(nums)
    print(result)
