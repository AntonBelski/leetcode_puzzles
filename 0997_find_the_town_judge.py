from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        incom_edges = [0] * n

        for a, b in trust:
            incom_edges[b - 1] += 1
            incom_edges[a - 1] -= 1

        for ind, edges in enumerate(incom_edges):
            if edges == n - 1:
                return ind + 1
        return -1


if __name__ == '__main__':
    solution = Solution()
    n = 3
    trust = [[1, 3], [2, 3], [3, 1]]
    result = solution.findJudge(n, trust)
    print(result)
