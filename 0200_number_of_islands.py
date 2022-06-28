from typing import List


class UnionFind:
    def __init__(self, n):
        self.nodes = []
        self.sizes = []

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
        else:
            self.nodes[root_p] = root_q
            self.sizes[root_q] += self.sizes[root_p]

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def root(self, p):
        while p != self.nodes[p]:
            p, self.nodes[p] = self.nodes[p], self.nodes[self.nodes[p]]
        return p


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        islands = set()
        union_find = UnionFind(rows * cols)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != '1':
                    continue

                if r > 0 and grid[r - 1][c] == '1':
                    union_find.union(r * cols + c, (r - 1) * cols + c)
                if c > 0 and grid[r][c - 1] == '1':
                    union_find.union(r * cols + c, r * cols + c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    islands.add(union_find.root(r * cols + c))

        return len(islands)


if __name__ == '__main__':
    solution = Solution()
    nums = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
    res = solution.numIslands(nums)
    print(res)
