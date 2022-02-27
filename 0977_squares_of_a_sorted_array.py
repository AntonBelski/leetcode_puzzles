from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums) - 1
        result = []

        while r >= l:
            if nums[r] ** 2 > nums[l] ** 2:
                result.append(nums[r] ** 2)
                r -= 1
            else:
                result.append(nums[l] ** 2)
                l += 1

        return result[::-1]


if __name__ == '__main__':
    solution = Solution()
    nums = [-4, -1, 0, 3, 10]
    res = solution.sortedSquares(nums)
    print(res)
