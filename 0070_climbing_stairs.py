class Solution:
    def climbStairs(self, n: int) -> int:
        # Fibonacci number, Time Complexity - O(n), Space Complexity - O(1)
        prev, curr = 1, 2
        for _ in range(n - 1):
            prev, curr = curr, prev + curr

        return prev

    def climbStairs2(self, n: int) -> int:
        # Bottom-up, Dynamic Programming, Time Complexity - O(n), Space Complexity - O(n)
        steps = [1, 2]

        for _ in range(2, n):
            steps.append(steps[-2] + steps[-1])

        return steps[n - 1]

    def climbStairs3(self, n: int) -> int:
        # Recursion + Memoization, Dynamic Programming, Time Complexity - O(n), Space Complexity - O(n)
        memo = [1, 2]

        def get_fibonacci(n, memo):
            if n < len(memo):
                return memo[n]

            memo.append(get_fibonacci(n - 2, memo) + get_fibonacci(n - 1, memo))
            return memo[-1]

        return get_fibonacci(n - 1, memo)


if __name__ == '__main__':
    solution = Solution()
    result = solution.climbStairs(10)
    print(result)
    result = solution.climbStairs2(10)
    print(result)
    result = solution.climbStairs3(10)
    print(result)
