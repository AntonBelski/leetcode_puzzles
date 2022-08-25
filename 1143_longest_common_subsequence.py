from typing import List


class Solution:
    def longestCommonSubsequence2(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text1) + 1) for _ in range(len(text2) + 1)]
        for r in range(len(text2)):
            for c in range(len(text1)):
                dp[r + 1][c + 1] = max(dp[r][c + 1], dp[r + 1][c])
                if text2[r] == text1[c]:
                    dp[r + 1][c + 1] = max(dp[r + 1][c + 1], dp[r][c] + 1)

        return dp[-1][-1]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp_prev, dp_curr = [0] * (len(text1) + 1), [0]
        for r in range(len(text2)):
            for c in range(len(text1)):
                new_val = max(dp_curr[c], dp_prev[c + 1])
                if text2[r] == text1[c]:
                    new_val = max(new_val, dp_prev[c] + 1)
                dp_curr.append(new_val)

            dp_prev, dp_curr = dp_curr, [0]

        return dp_prev[-1]


if __name__ == '__main__':
    solution = Solution()
    text1 = "abcde"
    text2 = "ace"
    result = solution.longestCommonSubsequence(text1, text2)
    print(result)
    result = solution.longestCommonSubsequence2(text1, text2)
    print(result)
