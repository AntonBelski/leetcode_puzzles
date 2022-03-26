from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result = []

        for t in tokens:
            if not t[-1].isdigit():
                if t == '-':
                    result[-2] -= result[-1]
                elif t == '+':
                    result[-2] += result[-1]
                elif t == '*':
                    result[-2] *= result[-1]
                else:
                    result[-2] = int(result[-2] / result[-1])
                result.pop()
            else:
                result.append(int(t))

        return sum(result)


if __name__ == '__main__':
    solution = Solution()
    tokens = ["2","1","+","3","*"]
    result = solution.evalRPN(tokens)
    print(result)
