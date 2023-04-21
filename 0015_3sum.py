from typing import List


class Solution:
    # solution 1 with sorting, complexity - O(n^2)
    def twoSum(self, first, curr_num, result):
        l = 0
        r = len(curr_num) - 1

        while r > l:
            if first + curr_num[l] + curr_num[r] > 0:
                r -= 1
            elif first + curr_num[l] + curr_num[r] < 0:
                l += 1
            else:
                result.add((first, curr_num[l], curr_num[r]))
                l += 1

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        nums.sort()
        result = set()

        for i in range(len(nums) - 2):
            self.twoSum(first=nums[i], curr_num=nums[i + 1:], result=result)

        return [list(s) for s in result]

    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sets = set()

        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            while j < k:
                three_sum = nums[i] + nums[j] + nums[k]
                if three_sum == 0:
                    new_tuple = tuple([nums[i], nums[j], nums[k]])
                    sets.add(new_tuple)
                    j += 1
                    k -= 1
                elif three_sum > 0:
                    k -= 1
                else:
                    j += 1

        return sets


if __name__ == '__main__':
    solution = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    res = solution.threeSum(nums)
    print(res)
    res = solution.threeSum2(nums)
    print(res)
