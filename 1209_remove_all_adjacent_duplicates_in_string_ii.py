from typing import List


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        for c in s:
            if not stack or stack[-1][0] != c:
                stack.append([c, 1])
            else:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()

        return ''.join([pair[0] * pair[1] for pair in stack])


if __name__ == '__main__':
    solution = Solution()
    s = "abcd"
    k = 2
    result = solution.removeDuplicates(s, k)
    print(result)
