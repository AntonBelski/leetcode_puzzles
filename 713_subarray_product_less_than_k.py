from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        result = 0
        l = 0
        product = 1

        for r in range(len(nums)):
            product *= nums[r]
            while product >= k and r >= l:
                product //= nums[l]
                l += 1

            if r >= l:
                result += r + 1 - l

        return result


if __name__ == '__main__':
    solution = Solution()
    nums = [10, 5, 2, 6]
    target = 100
    res = solution.numSubarrayProductLessThanK(nums, target)
    print(res)
