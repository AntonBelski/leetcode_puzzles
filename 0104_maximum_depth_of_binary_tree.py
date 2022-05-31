from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # BFS, TC = O(n), SC = O(n)
        max_depth = 0
        deq = deque()
        if root:
            deq.append([root, 1])

        while deq:
            node, level = deq.popleft()
            if node.left:
                deq.append([node.left, level + 1])
            if node.right:
                deq.append([node.right, level + 1])
            if not node.left and not node.right:
                max_depth = max(max_depth, level)

        return max_depth

    def maxDepth2(self, root: Optional[TreeNode]) -> int:
        # DFS, TC = O(n), SC = O(n)
        self.max_depth = 0

        def dfs(node, level=1):
            if node.left:
                dfs(node.left, level + 1)
            if node.right:
                dfs(node.right, level + 1)
            if not node.left and not node.right:
                self.max_depth = max(self.max_depth, level)

        if root:
            dfs(root)
        return self.max_depth


if __name__ == '__main__':
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)

    solution = Solution()
    result = solution.maxDepth(root)
    print(result)
    result = solution.maxDepth2(root)
    print(result)
