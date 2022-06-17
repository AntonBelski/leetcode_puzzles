from typing import List


class Solution:
    def longestPalindrome(self, s: str) -> str:
        p = [0, 0]

        for i in range(len(s)):
            for start, end in [[i - 1, i + 1], [i, i + 1]]:
                while start >= 0 and end < len(s) and s[start] == s[end]:
                    if end - start > p[1] - p[0]:
                        p = [start, end]
                    start -= 1
                    end += 1

        return s[p[0]:p[1] + 1]


if __name__ == '__main__':
    solution = Solution()
    s = "babad"
    result = solution.longestPalindrome(s)
    print(result)
