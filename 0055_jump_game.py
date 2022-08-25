from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_jump = nums[0]
        ind = 0

        while ind + 1 < len(nums) and ind + 1 <= max_jump:
            ind += 1
            max_jump = max(ind + nums[ind], max_jump)

        return max_jump >= len(nums) - 1


if __name__ == '__main__':
    solution = Solution()
    nums = [2, 3, 1, 1, 4]
    result = solution.canJump(nums)
    print(result)
