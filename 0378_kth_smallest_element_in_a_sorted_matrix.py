from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        max_len = len(matrix)
        heap = [[row[0], ind, 0] for ind, row in enumerate(matrix)]
        heapify(heap)

        while k:
            k -= 1
            val, matr_ind, row_ind = heappop(heap)

            if row_ind + 1 < max_len:
                new_val = matrix[matr_ind][row_ind + 1]
                heappush(heap, [new_val, matr_ind, row_ind + 1])

        return val


if __name__ == '__main__':
    solution = Solution()
    matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
    k = 8
    result = solution.kthSmallest(matrix, k)
    print(result)
