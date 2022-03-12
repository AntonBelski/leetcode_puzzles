from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        even_count = 0

        for n in nums:
            even_count += (len(str(n)) % 2) ^ 1

        return even_count


if __name__ == '__main__':
    solution = Solution()
    nums = [12, 345, 2, 6, 7896]
    result = solution.findNumbers(nums)
    print(result)
