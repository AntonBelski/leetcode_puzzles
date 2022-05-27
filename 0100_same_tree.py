from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p, q):
        if p and q and p.val == q.val:
            return all([self.isSameTree(p.left, q.left),
                        self.isSameTree(p.right, q.right)])
        return p is None and q is None


if __name__ == '__main__':
    root_q = TreeNode(12)
    root_q.left = TreeNode(7)
    root_q.right = TreeNode(1)
    root_q.left.left = TreeNode(9)
    root_q.right.left = TreeNode(10)
    root_q.right.right = TreeNode(5)

    root_p = TreeNode(12)
    root_p.left = TreeNode(7)
    root_p.right = TreeNode(1)
    root_p.left.left = TreeNode(9)
    root_p.right.left = TreeNode(10)
    root_p.right.right = TreeNode(5)

    solution = Solution()
    result = solution.isSameTree(root_p, root_q)
    print(result)
