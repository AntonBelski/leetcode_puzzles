from typing import List


class Solution:
    def update_result(self, n, result):
        result.append([])
        for col in self.queens:
            row_text = ['.'] * n
            row_text[col] = 'Q'
            result[-1].append(''.join(row_text))

    def recursive_add_queens(self, n, result, row=0):
        if row >= n:
            self.update_result(n, result)
            return

        for col in range(n):
            # My code
            # up_down_ind = n - 1 - row + col
            # down_up_ind = 2 * n - 2 - row - col

            # Improved version from the leetcode solutions
            up_down_ind = row - col
            down_up_ind = row + col

            if (col not in self.cols and
                    up_down_ind not in self.up_down_diags and
                    down_up_ind not in self.down_up_diags):
                self.cols.add(col)
                self.up_down_diags.add(up_down_ind)
                self.down_up_diags.add(down_up_ind)

                self.queens.append(col)
                self.recursive_add_queens(n, result, row + 1)
                self.queens.pop()

                self.cols.remove(col)
                self.up_down_diags.remove(up_down_ind)
                self.down_up_diags.remove(down_up_ind)

    def solveNQueens(self, n: int) -> List[List[str]]:
        # Backtracking, TC = O(n!), SC = O(n)
        result = []
        self.queens = []
        self.cols = set()
        self.up_down_diags = set()
        self.down_up_diags = set()
        self.recursive_add_queens(n, result)
        return result


if __name__ == '__main__':
    solution = Solution()
    n = 4
    result = solution.solveNQueens(n)
    print(result)
