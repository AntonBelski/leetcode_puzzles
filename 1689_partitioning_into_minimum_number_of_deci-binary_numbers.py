from typing import List


class Solution:
    def minPartitions(self, n: str) -> int:
        return max(n)


if __name__ == '__main__':
    solution = Solution()
    n = "27346209830709182346"
    result = solution.minPartitions(n)
    print(result)
