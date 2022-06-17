from typing import List


class Solution:
    def minDistance2(self, w1, w2):
        # DP with 2D array, Time Complexity - O(n^2), Space Complexity - O(n^2).
        dp = [[0] for _ in range(len(w2) + 1)]
        dp[0] = [0] * (len(w1) + 1)

        for i in range(len(w2)):
            for j in range(len(w1)):
                if w1[j] == w2[i]:
                    dp[i + 1].append(dp[i][j] + 1)
                else:
                    dp[i + 1].append(max(dp[i + 1][j], dp[i][j + 1]))

        return len(w2) + len(w1) - 2 * dp[-1][-1]

    def minDistance(self, w1, w2):
        # DP with 1D array, Time Complexity - O(n^2), Space Complexity - O(n).
        dp = [0] * (len(w1) + 1)

        for i in range(len(w2)):
            pr = dp[0]
            for j in range(len(w1)):
                if w1[j] == w2[i]:
                    pr, dp[j + 1] = dp[j + 1], pr + 1
                else:
                    pr, dp[j + 1] = dp[j + 1], max(dp[j], dp[j + 1])

        return len(w2) + len(w1) - 2 * dp[-1]


if __name__ == '__main__':
    solution = Solution()
    word1 = "leetcode"
    word2 = "etco"
    result = solution.minDistance2(word1, word2)
    print(result)
    result = solution.minDistance(word1, word2)
    print(result)
