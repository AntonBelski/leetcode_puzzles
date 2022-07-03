from collections import deque
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        deq = deque()
        rows, cols = len(mat), len(mat[0])
        matrix = [[] for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    deq.append([r, c, 0])
                    matrix[r].append(1)
                else:
                    matrix[r].append(float('inf'))

        while deq:
            r, c, dist = deq.popleft()
            if not (0 <= r < rows and 0 <= c < cols):
                continue
            if dist >= matrix[r][c]:
                continue

            matrix[r][c] = dist
            for _r, _c in ((0, -1), (0, 1), (-1, 0), (1, 0)):
                deq.append([r + _r, c + _c, dist + 1])

        return matrix


if __name__ == '__main__':
    solution = Solution()
    mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
    result = solution.updateMatrix(mat)
    print(result)
