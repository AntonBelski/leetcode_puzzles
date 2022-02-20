from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return nums
        if len(nums) == 1:
            return [str(nums[0])]

        start = nums[0]
        i = 1
        result = []

        while i < len(nums):
            if abs(nums[i] - nums[i - 1]) > 1:
                if start == nums[i - 1]:
                    result.append(str(nums[i - 1]))
                else:
                    result.append(str(start) + '->' + str(nums[i - 1]))
                start = nums[i]
            i += 1

        if start == nums[-1]:
            result.append(str(nums[-1]))
        else:
            result.append(str(start) + '->' + str(nums[-1]))

        return result


if __name__ == '__main__':
    solution = Solution()
    nums = [0, 1, 2, 4, 5, 7]
    res = solution.summaryRanges(nums)
    print(res)
