from typing import List


class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for c in s:
            if not stack or stack[-1] != c:
                stack.append(c)
            else:
                stack.pop()

        return ''.join(stack)


if __name__ == '__main__':
    solution = Solution()
    s = "abbaca"
    result = solution.removeDuplicates(s)
    print(result)
