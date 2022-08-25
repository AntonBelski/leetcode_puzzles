from typing import List


class Solution:
    def jump2(self, nums: List[int]) -> int:
        n = len(nums)
        min_jumps = [float('inf')] * n
        min_jumps[0] = 0

        for ind in range(n - 1):
            num = nums[ind]
            for jump in range(ind + 1, min(ind + num + 1, n)):
                min_jumps[jump] = min(min_jumps[jump], min_jumps[ind] + 1)

        return min_jumps[-1]

    def jump(self, nums: List[int]) -> int:
        min_jumps = [float('inf')] * len(nums)
        min_jumps[0] = 0
        max_jump = 0

        for ind, num in enumerate(nums):
            if ind > max_jump:
                break
            for jump in range(max_jump + 1, min(ind + num + 1, len(nums))):
                min_jumps[jump] = min_jumps[ind] + 1
            max_jump = max(max_jump, ind + num)

        return min_jumps[-1]


if __name__ == '__main__':
    solution = Solution()
    nums = [2, 3, 1, 1, 4]
    result = solution.jump(nums)
    print(result)
    result = solution.jump2(nums)
    print(result)
