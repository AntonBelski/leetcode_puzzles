from typing import List


class Solution:
    def heightChecker(self, nums: List[int]) -> int:
        n = len(nums)
        places = [0] * 101

        for elem in nums:
            places[elem] += 1

        for i in range(1, 101):
            places[i] += places[i - 1]

        sorted_nums = [0] * n
        for elem in nums:
            sorted_nums[places[elem] - 1] = elem
            places[elem] -= 1

        result = 0
        for i in range(n):
            if sorted_nums[i] != nums[i]:
                result += 1

        return result


if __name__ == '__main__':
    solution = Solution()
    heights = [1, 1, 4, 2, 1, 3]
    result = solution.heightChecker(heights)
    print(result)
