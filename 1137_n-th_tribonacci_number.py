from typing import List


class Solution:
    def tribonacci(self, n: int) -> int:
        cache = {0: 0, 1: 1, 2: 1}
        def nth_ways(cache, n):
            if n in cache:
                return cache[n]
            cache[n] = nth_ways(cache, n - 3) + nth_ways(cache, n - 2) + nth_ways(cache, n - 1)
            return cache[n]

        return nth_ways(cache, n)


if __name__ == '__main__':
    solution = Solution()
    n = 10
    result = solution.tribonacci(10)
    print(result)
