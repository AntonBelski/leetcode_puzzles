from typing import List


class UnionFind:
    def __init__(self, grid):
        self.nodes = {}
        self.sizes = {}
        rows_len = len(grid)
        columns_len = len(grid[0])

        for i in range(rows_len):
            for j in range(columns_len):
                self.nodes[i * columns_len + j] = i * columns_len + j
                self.sizes[i * columns_len + j] = 1

    def root(self, p):
        while p != self.nodes[p]:
            self.nodes[p] = self.nodes[self.nodes[p]]
            p = self.nodes[p]

        return p

    def union(self, p, q):
        root_p = self.root(p)
        root_q = self.root(q)

        if self.sizes[root_p] > self.sizes[root_q]:
            self.nodes[root_q] = root_p
            self.sizes[root_p] += self.sizes[root_q]
        else:
            self.nodes[root_p] = root_q
            self.sizes[root_q] += self.sizes[root_p]

    def connected(self, p, q):
        return self.root(p) == self.root(q)


class Solution:
    def maxAreaOfIsland(self, grid: List[List[str]]) -> int:
        islands = dict()
        rows_len = len(grid)
        columns_len = len(grid[0])
        union_find = UnionFind(grid)

        for i in range(rows_len):
            for j in range(columns_len):
                if i > 0 and grid[i][j] == grid[i - 1][j] == 1:
                    union_find.union(i * columns_len + j, (i - 1) * columns_len + j)
                if i < rows_len - 1 and grid[i][j] == grid[i + 1][j] == 1:
                    union_find.union(i * columns_len + j, (i + 1) * columns_len + j)
                if j > 0 and grid[i][j] == grid[i][j - 1] == 1:
                    union_find.union(i * columns_len + j, i * columns_len + j - 1)
                if j < columns_len - 1 and grid[i][j] == grid[i][j + 1] == 1:
                    union_find.union(i * columns_len + j, i * columns_len + j + 1)

        for i in range(rows_len):
            for j in range(columns_len):
                if grid[i][j] == 1:
                    current_root = union_find.root(i * columns_len + j)
                    if current_root in islands:
                        islands[current_root] += 1
                    else:
                        islands[current_root] = 1

        return max(islands.values()) if islands else 0


if __name__ == '__main__':
    solution = Solution()
    nums = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    res = solution.maxAreaOfIsland(nums)
    print(res)
