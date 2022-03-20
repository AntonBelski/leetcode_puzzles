from typing import List


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # My Solution, Time Complexity - O(n), Space Complexity - O(n)
        stack = [0]
        result = 0

        for c in s:
            if c == '(':
                stack.append(0)
            elif len(stack) > 1:
                cost = stack.pop()
                stack[-1] += cost + 2
                result = max(result, stack[-1])
            else:
                stack = [0]

        return result

    def longestValidParentheses2(self, s: str) -> int:
        # Very Smart Solution, Time Complexity - O(n), Space Complexity - O(1)
        result = 0
        open_b = close_b = 0

        for c in s:
            if c == '(':
                open_b += 1
            else:
                open_b += 1
                if open_b == close_b:
                    result = max(result, 2 * close_b)
                elif close_b > open_b:
                    close_b = open_b = 0

        open_b = close_b = 0
        for c in s[::-1]:
            if c == ')':
                open_b += 1
            else:
                close_b += 1
                if open_b == close_b:
                    result = max(result, 2 * close_b)
                elif close_b > open_b:
                    close_b = open_b = 0

        return result


if __name__ == '__main__':
    solution = Solution()
    s = "(()"
    result = solution.longestValidParentheses(s)
    print(result)
    result = solution.longestValidParentheses2(s)
    print(result)
