from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = nums[0]
        max_count = count

        for n in nums[1:]:
            if n == 1:
                count += 1
            else:
                count = 0

            max_count = max(max_count, count)

        return max_count


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 0, 1, 1, 0, 1]
    result = solution.findMaxConsecutiveOnes(nums)
    print(result)
