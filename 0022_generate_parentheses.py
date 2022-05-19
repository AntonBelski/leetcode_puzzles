from typing import List


class Solution:
    # Time Complexity - O(4^n), Space Complexity - O(n).
    def recursive_parentheses(self, result, balance=0, ind=0):
        if ind == self.n * 2 or balance < 0 or balance > self.n:
            if balance == 0:
                result.append(''.join(self.cur))
            return

        for p in self.parentheses:
            new_balance = balance + self.parentheses[p]
            self.cur.append(p)
            self.recursive_parentheses(result, new_balance, ind + 1)
            self.cur.pop()

    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.parentheses = {'(': 1, ')': -1}
        self.cur = []
        self.n = n
        self.recursive_parentheses(result)
        return result


if __name__ == '__main__':
    solution = Solution()
    n = 3
    result = solution.generateParenthesis(n)
    print(result)
