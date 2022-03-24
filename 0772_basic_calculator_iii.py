from typing import List


class Solution:
    # Solution for the Basic Calculator I, II and III
    def tokenize(self, s):
        number_str = []
        for c in s:
            if c.isdigit():
                number_str.append(c)
            else:
                if number_str:
                    yield ''.join(number_str)
                    number_str = []
                yield c

        if number_str:
            yield ''.join(number_str)

    def calculate(self, s):
        if type(s) == str:
            s = self.tokenize(s)

        result = []
        op = '+'

        for c in s:
            if c == '(':
                val = self.calculate(s)
            elif c == ')':
                break
            elif c in '+-*/ ':
                if c != ' ':
                    op = c
                continue
            else:
                val = int(c)

            if op == '-':
                result.append(-val)
            elif op == '+':
                result.append(val)
            elif op == '*':
                result[-1] *= val
            elif op == '/':
                # because -3 // 2 = -2 (we want -1)
                result[-1] = int(result[-1] / val)

        return sum(result)


if __name__ == '__main__':
    solution = Solution()
    s = "2*(5+5*2)/3+(6/2+8)"
    result = solution.calculate(s)
    print(result)
