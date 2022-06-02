from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = [nums[0]]
        for n in nums[1:]:
            result.append(result[-1] + n)
        return result


if __name__ == '__main__':
    solution = Solution()
    nums = [3, 1, 2, 10, 1]
    result = solution.runningSum(nums)
    print(result)
