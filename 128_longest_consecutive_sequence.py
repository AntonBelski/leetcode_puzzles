from typing import List


class UnionFind:
    def __init__(self, nums):
        # Time Complexity - O(n)
        self.nodes = {}
        self.sizes = {}

        for elem in nums:
            self.nodes[elem] = elem
        for elem in range(len(nums)):
            self.sizes[elem] = 1

    def union(self, p, q):
        # Time Complexity - O(log*(n)), * -> this function veryyy close to constant O(1)
        p_node_root = self.root(p)
        q_node_root = self.root(q)
        if self.sizes[q_node_root] > self.sizes[p_node_root]:
            self.nodes[p_node_root] = q_node_root
            self.sizes[q_node_root] += self.sizes[p_node_root]
        else:
            self.nodes[q_node_root] = p_node_root
            self.sizes[p_node_root] += self.sizes[q_node_root]

    def root(self, e):
        # Time Complexity - O(log*(n)), * -> this function veryyy close to constant O(1)
        while e != self.nodes[e]:
            self.nodes[e] = self.nodes[self.nodes[e]]
            e = self.nodes[e]
        return e

    def connected(self, p, q):
        # Time Complexity - O(log*(n)), * -> this function veryyy close to constant O(1)
        return self.root(p) == self.root(q)


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        union_find = UnionFind(nums)
        checked_dict = {}

        for elem in nums:
            if elem in checked_dict:
                continue
            checked_dict[elem] = True
            if elem + 1 in checked_dict:
                union_find.union(elem, elem + 1)
            if elem - 1 in checked_dict:
                union_find.union(elem, elem - 1)

        max_size = max(union_find.sizes.values())

        return max_size


if __name__ == '__main__':
    solution = Solution()
    nums = [100, 4, 200, 1, 3, 2]
    res = solution.longestConsecutive(nums)
    print(res)
