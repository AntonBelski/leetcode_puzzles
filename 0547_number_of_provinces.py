from typing import List


class UnionFind:
    def __init__(self, n):
        self.nodes = []
        self.sizes = []
        self.provinces = n

        for i in range(n):
            self.nodes.append(i)
            self.sizes.append(1)

    def union(self, p, q):
        root_p = self.root(p)
        root_q = self.root(q)

        if root_p == root_q:
            return

        self.provinces -= 1

        if self.sizes[root_p] > self.sizes[root_q]:
            self.nodes[root_q] = root_p
            self.sizes[root_p] += self.sizes[root_q]
        else:
            self.nodes[root_p] = root_q
            self.sizes[root_q] += self.sizes[root_p]

    def root(self, p):
        while p != self.nodes[p]:
            p, self.nodes[p] = self.nodes[p], self.nodes[self.nodes[p]]
        return p


class Solution:
    def findCircleNum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        union_find = UnionFind(n)

        for p in range(n):
            for q in range(p + 1, n):
                if matrix[p][q] == 1:
                    union_find.union(p, q)

        return union_find.provinces


if __name__ == '__main__':
    solution = Solution()
    nums = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    res = solution.findCircleNum(nums)
    print(res)
