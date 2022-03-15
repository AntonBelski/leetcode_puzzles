from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        max_nums = set()

        for elem in nums:
            if len(max_nums) < 3:
                max_nums.add(elem)
            elif elem > min(max_nums) and elem not in max_nums:
                max_nums.remove(min(max_nums))
                max_nums.add(elem)

        if len(max_nums) < 3:
            return max(max_nums)
        else:
            return min(max_nums)


if __name__ == '__main__':
    solution = Solution()
    nums = [3, 2, 1]
    result = solution.thirdMax(nums)
    print(result)
