class Solution:
    def singleNumber(self, nums) -> int:
        result = 0
        for elem in nums:
            result ^= elem
        return result


if __name__ == '__main__':
    solution = Solution()
    my_nums = [2, 2, 1]
    result = solution.singleNumber(my_nums)
    print(result)
