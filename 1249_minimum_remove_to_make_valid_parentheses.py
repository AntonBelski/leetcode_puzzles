from typing import List


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        result = []
        counter = 0

        for ch in s:
            if ch == '(':
                counter += 1
                result.append(ch)
            elif ch == ')':
                if counter > 0:
                    counter -= 1
                    result.append(ch)
            else:
                result.append(ch)

        counter = 0
        n = len(result)

        for i in range(n):
            ch = result[n - 1 - i]
            if ch == ')':
                counter += 1
            elif ch == '(':
                if counter > 0:
                    counter -= 1
                else:
                    result[n - 1 - i] = ''

        return ''.join(result)


if __name__ == '__main__':
    solution = Solution()
    s = "lee(t(c)o)de)"
    result = solution.minRemoveToMakeValid(s)
    print(result)
