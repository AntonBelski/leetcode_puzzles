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
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if n > len(connections) + 1:
            return -1
        union_find = UnionFind(n)

        for p, q in connections:
            union_find.union(p, q)

        return union_find.provinces - 1


if __name__ == '__main__':
    solution = Solution()
    n = 4
    connections = [[0, 1], [0, 2], [1, 2]]
    result = solution.makeConnected(n, connections)
    print(result)
