from typing import List


class Solution:
    # Time Complexity - O(n * 2^n), Space Complexity - O(n).
    def letterCasePermutation(self, s: str) -> List[str]:
        result = []
        self.current = []
        self.swapcase_backtrack(s, result)
        return result

    def swapcase_backtrack(self, s, result, first=0):
        if first == len(s):
            result.append(''.join(self.current))
            return
        self.current.append(s[first])
        self.swapcase_backtrack(s, result, first + 1)
        self.current.pop()

        if s[first].isalpha():
            self.current.append(s[first].swapcase())
            self.swapcase_backtrack(s, result, first + 1)
            self.current.pop()


if __name__ == '__main__':
    solution = Solution()
    s = "a1b2"
    result = solution.letterCasePermutation(s)
    print(result)
