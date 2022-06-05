from typing import List


class UnionFind:
    def __init__(self, n):
        self.sizes = []
        self.nodes = []
        self.connected_components = n
        self.path_size = 0

        for i in range(n):
            self.nodes.append(i)
            self.sizes.append(1)

    def union(self, p, q, w):
        p_root_node = self.root(p)
        q_root_node = self.root(q)
        self.path_size += w
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
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        union_find = UnionFind(n)
        sorted_cons = sorted(connections, key=lambda x: x[2])

        for p, q, w in sorted_cons:
            if union_find.root(p - 1) != union_find.root(q - 1):
                union_find.union(p - 1, q - 1, w)

        if union_find.connected_components == 1:
            return union_find.path_size
        else:
            return -1


if __name__ == '__main__':
    solution = Solution()
    n = 3
    connections = [[1, 2, 5], [1, 3, 6], [2, 3, 1]]
    result = solution.minimumCost(n, connections)
    print(result)
