from typing import List


class Solution:
    def minimumTotal(self, trn):
        for i in range(len(trn) - 1, 0, -1):
            for j in range(i):
                trn[i - 1][j] += min(trn[i][j], trn[i][j + 1])
        return trn[0][0]


if __name__ == '__main__':
    solution = Solution()
    triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    result = solution.minimumTotal(triangle)
    print(result)
