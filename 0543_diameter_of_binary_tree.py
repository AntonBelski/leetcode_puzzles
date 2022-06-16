from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0
            left_path = dfs(node.left)
            right_path = dfs(node.right)
            self.max_diameter = max(self.max_diameter, left_path + right_path)
            return max(left_path, right_path) + 1

        self.max_diameter = 0
        dfs(root)
        return self.max_diameter


if __name__ == '__main__':
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)

    solution = Solution()
    result = solution.diameterOfBinaryTree(root)
    print(result)
