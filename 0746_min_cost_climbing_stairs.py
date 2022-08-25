from typing import List


class Solution:
    def minCostClimbingStairs3(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [float('inf')] * (n + 2)
        dp[0], dp[1] = cost[0], cost[1]

        for i in range(n):
            cost_one_jump = cost[i + 1] if i + 1 < n else 0
            dp[i + 1] = min(dp[i + 1], dp[i] + cost_one_jump)
            cost_two_jumps = cost[i + 2] if i + 2 < n else 0
            dp[i + 2] = min(dp[i + 2], dp[i] + cost_two_jumps)

        return dp[-2]

    def minCostClimbingStairs2(self, cost: List[int]) -> int:
        curr, jump, n = cost[0], cost[1], len(cost)

        for i in range(len(cost)):
            cost1 = cost[i + 1] if i + 1 < n else 0
            cost2 = cost[i + 2] if i + 2 < n else 0
            curr, jump = min(jump, curr + cost1), curr + cost2

        return curr

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        two = one = 0

        for i in range(2, len(cost) + 1):
            two, one = one, min(one + cost[i - 1], two + cost[i - 2])

        return one


if __name__ == '__main__':
    solution = Solution()
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    result = solution.minCostClimbingStairs(cost)
    print(result)
    result = solution.minCostClimbingStairs2(cost)
    print(result)
    result = solution.minCostClimbingStairs3(cost)
    print(result)
