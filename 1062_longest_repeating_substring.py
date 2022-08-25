from typing import List


class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        dp = [[0] * (len(s) + 1) for _ in range(len(s) + 1)]
        res = 0

        for r in range(len(s)):
            for c in range(len(s)):
                if c > r:
                    if s[r] == s[c]:
                        dp[r + 1][c + 1] = dp[r][c] + 1
                    else:
                        dp[r + 1][c + 1] = 0
                    res = max(res, dp[r + 1][c + 1])

        return res


if __name__ == '__main__':
    solution = Solution()
    s = "abbaba"
    result = solution.longestRepeatingSubstring(s)
    print(result)
