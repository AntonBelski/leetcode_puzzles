from typing import List


class Solution:
    def isValid(self, s: str) -> bool:
        reverse_brackets = {')': '(', ']': '[', '}': '{'}
        stack = []

        for c in s:
            if c in reverse_brackets.values():
                stack.append(c)
            elif stack and reverse_brackets[c] == stack[-1]:
                stack.pop()
            else:
                return False

        return False if stack else True


if __name__ == '__main__':
    solution = Solution()
    s = "()[]{}"
    res = solution.isValid(s)
    print(res)
