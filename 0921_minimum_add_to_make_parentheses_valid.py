from typing import List


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_brackets = 0
        for c in s:
            if c == '(':
                open_brackets += 1
            elif c == ')' and open_brackets > 0:
                open_brackets -= 1

        close_brackets = 0
        for c in s[::-1]:
            if c == ')':
                close_brackets += 1
            elif c == '(' and close_brackets > 0:
                close_brackets -= 1

        return open_brackets + close_brackets


if __name__ == '__main__':
    solution = Solution()
    s = "())"
    result = solution.minAddToMakeValid(s)
    print(result)
