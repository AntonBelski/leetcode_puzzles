from typing import List


class UnionFind:
    def __init__(self, n):
        self.sizes = []
        self.nodes = []
        self.connected_components = n

        for i in range(n):
            self.nodes.append(i)
            self.sizes.append(1)

    def union(self, p, q):
        p_root_node = self.root(p)
        q_root_node = self.root(q)
        if p_root_node != q_root_node:
            self.connected_components -= 1

        if self.sizes[p_root_node] > self.sizes[q_root_node]:
            self.nodes[q_root_node] = p_root_node
            self.sizes[q_root_node] += self.sizes[p_root_node]
        else:
            self.nodes[p_root_node] = q_root_node
            self.sizes[p_root_node] += self.sizes[q_root_node]

    def root(self, e):
        while e != self.nodes[e]:
            self.nodes[e] = self.nodes[self.nodes[e]]
            e = self.nodes[e]
        return e


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        union_find = UnionFind(n)
        for p, q in edges:
            union_find.union(p, q)

        return union_find.connected_components


if __name__ == '__main__':
    solution = Solution()
    n = 5
    edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
    result = solution.countComponents(n, edges)
    print(result)
