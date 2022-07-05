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
    def longestConsecutive1(self, nums: List[int]) -> int:
        # First solution with Union Find (My Solution)
        # Time Complexity - O(n + m * log*(n)), * -> this function veryyy close to constant O(1)
        # Space Complexity - O(n)
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

    def longestConsecutive2(self, nums: List[int]) -> int:
        # Second solution with Sets (My Solution)
        # Time Complexity - O(n), Space Complexity - O(n)
        uniq_nums = set(nums)
        used_nums = set()
        result = 0

        for num in nums:
            if num in used_nums:
                continue

            curr_res = 1
            used_nums.add(num)

            left_num = num - 1
            while left_num in uniq_nums:
                curr_res += 1
                used_nums.add(left_num)
                left_num -= 1

            right_num = num + 1
            while right_num in uniq_nums:
                curr_res += 1
                used_nums.add(right_num)
                right_num += 1

            result = max(result, curr_res)

        return result

    def longestConsecutive3(self, nums: List[int]) -> int:
        # Second solution with sets (From Leetcode Solutions)
        # Time Complexity - O(n), Space Complexity - O(n)
        longest_streak = 0
        nums_set = set(nums)

        for elem in nums_set:
            if elem - 1 not in nums_set:
                curr_streak = 1
                curr_elem = elem

                while curr_elem + 1 in nums_set:
                    curr_elem += 1
                    curr_streak += 1

                longest_streak = max(longest_streak, curr_streak)

        return longest_streak


if __name__ == '__main__':
    solution = Solution()
    nums = [100, 4, 200, 1, 3, 2]
    result = solution.longestConsecutive1(nums)
    print(result)
    result = solution.longestConsecutive2(nums)
    print(result)
    result = solution.longestConsecutive3(nums)
    print(result)
