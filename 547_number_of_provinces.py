from typing import List


class UnionFind:
    def __init__(self, nums):
        self.nodes = {}
        self.sizes = {}

        for i in range(nums):
            self.nodes[i] = i
            self.sizes[i] = 1

    def root(self, p):
        while p != self.nodes[p]:
            self.nodes[p] = self.nodes[self.nodes[p]]
            p = self.nodes[p]

        return p

    def union(self, p, q):
        root_p = self.root(p)
        root_q = self.root(q)

        if self.nodes[root_p] > self.nodes[root_q]:
            self.nodes[root_q] = root_p
            self.sizes[root_p] += self.sizes[root_q]
        else:
            self.nodes[root_p] = root_q
            self.sizes[root_q] += self.sizes[root_p]


class Solution:
    def findCircleNum(self, grid: List[List[int]]) -> int:
        provinces = set()
        columns_len = len(grid)
        union_find = UnionFind(len(grid))

        for i in range(columns_len):
            for j in range(columns_len):
                if grid[i][j] == 1 and i != j:
                    union_find.union(i, j)

        for i in range(columns_len):
            root_elem = union_find.root(i)
            provinces.add(root_elem)

        return len(provinces)


if __name__ == '__main__':
    solution = Solution()
    nums = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    res = solution.findCircleNum(nums)
    print(res)
