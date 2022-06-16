from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        curr_sum = 0
        uniq_nums = set()
        start = 0
        result = 0

        for n in nums:
            while n in uniq_nums:
                uniq_nums.remove(nums[start])
                curr_sum -= nums[start]
                start += 1
            uniq_nums.add(n)
            curr_sum += n
            result = max(result, curr_sum)

        return result


if __name__ == '__main__':
    solution = Solution()
    nums = [4, 2, 4, 5, 6]
    result = solution.maximumUniqueSubarray(nums)
    print(result)
