from typing import List


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self.pref_sum = [[0] * (cols + 1)]
        for r in range(rows):
            pref = [0]
            self.pref_sum.append([0])
            for c in range(cols):
                pref.append(pref[-1] + matrix[r][c])
                pref_val = pref[-1] + self.pref_sum[r][c + 1]
                self.pref_sum[r + 1].append(pref_val)

    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        right_bottom = self.pref_sum[r2 + 1][c2 + 1]
        right_top = self.pref_sum[r1][c2 + 1]
        left_bottom = self.pref_sum[r2 + 1][c1]
        left_top = self.pref_sum[r1][c1]
        return right_bottom - right_top - left_bottom + left_top


if __name__ == '__main__':
    num_matrix = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
    result = num_matrix.sumRegion(2, 1, 4, 3)
    print(result)
    result = num_matrix.sumRegion(1, 1, 2, 2)
    print(result)
    result = num_matrix.sumRegion(1, 2, 2, 4)
    print(result)
