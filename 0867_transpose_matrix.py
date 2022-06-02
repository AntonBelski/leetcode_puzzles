from typing import List


class Solution:
    def transpose2(self, matrix: List[List[int]]) -> List[List[int]]:
        result = [[] for _ in matrix[0]]
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                result[c].append(matrix[r][c])
        return result

    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return list(zip(*matrix))


if __name__ == '__main__':
    solution = Solution()
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result = solution.transpose(matrix)
    print(result)
    result = solution.transpose2(matrix)
    print(result)
