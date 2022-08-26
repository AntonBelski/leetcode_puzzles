from typing import List


class Solution:
    def maximumXOR(self, nums: List[int]) -> int:
        res = nums[0]
        for i in range(1, len(nums)):
            res |= nums[i]
        return res


if __name__ == '__main__':
    solution = Solution()
    nums = [3, 2, 4, 6]
    result = solution.maximumXOR(nums)
    print(result)
