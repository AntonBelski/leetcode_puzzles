from typing import List


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        rows_len = len(matrix)
        columns_len = len(matrix[0])
        self.prefix_matrix = [[] for _ in range(rows_len)]

        for r in range(rows_len):
            prefix_row = 0
            for c in range(columns_len):
                curr_sum = matrix[r][c]
                curr_sum += self.prefix_matrix[r - 1][c] if r >= 1 else 0
                curr_sum += prefix_row
                prefix_row += matrix[r][c]
                self.prefix_matrix[r].append(curr_sum)

    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        result = self.prefix_matrix[r2][c2]
        if c1 >= 1:
            result -= self.prefix_matrix[r2][c1 - 1]
        if r1 >= 1:
            result -= self.prefix_matrix[r1 - 1][c2]
        if c1 >= 1 and r1 >= 1:
            result += self.prefix_matrix[r1 - 1][c1 - 1]
        return result


if __name__ == '__main__':
    num_matrix = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
    result = num_matrix.sumRegion(2, 1, 4, 3)
    print(result)
    result = num_matrix.sumRegion(1, 1, 2, 2)
    print(result)
    result = num_matrix.sumRegion(1, 2, 2, 4)
    print(result)
