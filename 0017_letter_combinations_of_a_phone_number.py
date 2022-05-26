from typing import List


class Solution:
    def recursive_next_number(self, result, ind=0):
        if ind == len(self.digits):
            if self.cur:
                result.append(''.join(self.cur))
            return

        next_number = self.digits[ind]
        for c in self.phone_dict[next_number]:
            self.cur.append(c)
            self.recursive_next_number(result, ind + 1)
            self.cur.pop()

    def letterCombinations(self, digits: str) -> List[str]:
        """
        TC = O(N * 4^N), N = len(digits)
        SC = O(N)
        """
        self.phone_dict = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        self.digits = digits
        self.cur = []
        result = []
        self.recursive_next_number(result)
        return result


if __name__ == '__main__':
    solution = Solution()
    digits = "23"
    result = solution.letterCombinations(digits)
    print(result)
