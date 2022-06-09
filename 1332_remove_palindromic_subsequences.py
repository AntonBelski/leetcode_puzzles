from typing import List


class Solution:
    def removePalindromeSub(self, s: str) -> int:
        for i in range(len(s) // 2):
            if s[i] != s[len(s) - 1 - i]:
                return 2
        return 1


if __name__ == '__main__':
    solution = Solution()
    s = "ababa"
    result = solution.removePalindromeSub(s)
    print(result)
