from typing import List


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        rows_len = len(mat)
        cols_len = len(mat[0])
        sorted_mat = [[] for _ in range(rows_len)]

        def sort_matrix(sorted_mat, is_vert, boundary, custom_range):
            for diag in custom_range:
                diag_arr = []

                for row, col in enumerate(range(diag, boundary)):
                    if is_vert:
                        row, col = col, row
                    if col >= cols_len or row >= rows_len:
                        break
                    diag_arr.append(mat[row][col])

                diag_arr.sort(reverse=True)

                for row in range(rows_len):
                    if not diag_arr:
                        break
                    if not is_vert or row >= diag:
                        sorted_mat[row].append(diag_arr.pop())

        sort_matrix(sorted_mat, True, rows_len, range(rows_len - 1, 0, -1))
        sort_matrix(sorted_mat, False, cols_len, range(cols_len))

        return sorted_mat


if __name__ == '__main__':
    solution = Solution()
    mat = [[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]]
    result = solution.diagonalSort(mat)
    print(result)
