from typing import List


class UnionFind:
    def __init__(self, n):
        self.nodes = []
        self.sizes = []
        self.max_island = 0

        for i in range(n):
            self.nodes.append(i)
            self.sizes.append(1)

    def union(self, p, q):
        root_p = self.root(p)
        root_q = self.root(q)

        if root_p == root_q:
            return

        if self.sizes[root_p] > self.sizes[root_q]:
            self.nodes[root_q] = root_p
            self.sizes[root_p] += self.sizes[root_q]
            self.max_island = max(self.max_island, self.sizes[root_p])
        else:
            self.nodes[root_p] = root_q
            self.sizes[root_q] += self.sizes[root_p]
            self.max_island = max(self.max_island, self.sizes[root_q])

    def root(self, p):
        while p != self.nodes[p]:
            p, self.nodes[p] = self.nodes[p], self.nodes[self.nodes[p]]
        return p


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows_len, cols_len = len(grid), len(grid[0])
        union_find = UnionFind(rows_len * cols_len)

        for r in range(rows_len):
            for c in range(cols_len):
                if grid[r][c] != 1:
                    continue
                union_find.max_island = max(union_find.max_island, 1)

                if r > 0 and grid[r - 1][c] == 1:
                    union_find.union(r * cols_len + c, (r - 1) * cols_len + c)
                if c > 0 and grid[r][c - 1] == 1:
                    union_find.union(r * cols_len + c, r * cols_len + c - 1)

        return union_find.max_island


if __name__ == '__main__':
    solution = Solution()
    nums = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    res = solution.maxAreaOfIsland(nums)
    print(res)
