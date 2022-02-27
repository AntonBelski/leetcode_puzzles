class Solution:
    def maxProfit(self, prices) -> int:
        min_value = prices[0]
        max_value = min_value
        profit = 0
        for elem in prices[1:]:
            if elem < min_value:
                min_value = elem
                max_value = elem
            if elem > max_value:
                max_value = elem
            curr_profit = max_value - min_value
            if curr_profit > profit:
                profit = curr_profit

        return profit


if __name__ == '__main__':
    solution = Solution()
    my_nums = [7, 1, 5, 3, 6, 4]
    result = solution.maxProfit(my_nums)
    print(result)
