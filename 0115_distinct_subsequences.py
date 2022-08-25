from typing import List


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp_prev = [0] * (len(s) + 1)
        res = 0

        for r in range(len(t)):
            dp_curr = [0]
            for c in range(r, len(s)):
                dp_curr.append(dp_curr[-1])
                if s[c] == t[r]:
                    dp_curr[-1] += dp_prev[c - r + 1] + (r == 0)
            dp_prev = dp_curr

        return dp_prev[-1]


if __name__ == '__main__':
    solution = Solution()
    s = "rabbbit"
    t = "rabbit"
    result = solution.numDistinct(s, t)
    print(result)
