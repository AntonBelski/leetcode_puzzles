from functools import lru_cache
from typing import List


class Solution:
    def fib4(self, n: int) -> int:
        # First solution with simple fibonacci number calculation
        # Time Complexity - O(n), Space Complexity - O(1)
        prev, curr = 0, 1
        for _ in range(n):
            prev, curr = curr, prev + curr

        return prev

    def fib3(self, n: int) -> int:
        # Second solution with DP, Bottom-Up Approach with Tabulation
        # Time Complexity - O(n), Space Complexity - O(n)
        cache = [0] * (n + 2)
        cache[1] = 1

        for i in range(2, n + 1):
            cache[i] = cache[i - 2] + cache[i - 1]

        return cache[n]

    def fib2(self, n: int) -> int:
        # Third solution with DP, Top-Down Approach with Memoization
        # Time Complexity - O(n), Space Complexity - O(n)
        cache = {0: 0, 1: 1}

        def fibonacci(cache, n):
            if n in cache:
                return cache[n]

            cache[n] = fibonacci(cache, n - 2) + fibonacci(cache, n - 1)
            return cache[n]

        return fibonacci(cache, n)

    @lru_cache
    def fib(self, n: int) -> int:
        # Third solution with DP, Top-Down Approach with Memoization using lru_cache
        # Time Complexity - O(n), Space Complexity - O(n)
        if n < 2:
            return n
        return self.fib(n - 2) + self.fib(n - 1)


if __name__ == '__main__':
    solution = Solution()
    n = 10
    result = solution.fib(n)
    print(result)
    result = solution.fib2(n)
    print(result)
    result = solution.fib3(n)
    print(result)
    result = solution.fib4(n)
    print(result)
