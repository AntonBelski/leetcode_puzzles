from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        all_xor = 0

        for num in nums:
            all_xor ^= num

        rightmost_bit = all_xor & (-all_xor)
        x = 0

        for num in nums:
            if num & rightmost_bit:
                x ^= num

        y = all_xor ^ x
        return [x, y]


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 2, 1, 3, 2, 5]
    result = solution.singleNumber(nums)
    print(result)
