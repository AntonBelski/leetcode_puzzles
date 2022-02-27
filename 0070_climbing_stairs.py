class Solution:
    def climbStairs(self, n: int) -> int:
        memo = []
        for i in range(n + 2):
            memo.append(self.fib(i, memo))

        return memo[n + 1]

    def fib(self, n, memo):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n < len(memo):
            return memo[n]

        return self.fib(n - 1, memo) + self.fib(n - 2, memo)


if __name__ == '__main__':
    solution = Solution()
    result = solution.climbStairs(3)
    print(result)
