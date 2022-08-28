from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        uniq_balances = {0: 0}
        balances_dict = {0: -1, 1: 1}
        result = balance = 0

        for ind, num in enumerate(nums):
            balance += balances_dict[num]
            if balance in uniq_balances:
                result = max(result, ind + 1 - uniq_balances[balance])
            else:
                uniq_balances[balance] = ind + 1

        return result


if __name__ == '__main__':
    solution = Solution()
    nums = [0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1]
    result = solution.findMaxLength(nums)
    print(result)
