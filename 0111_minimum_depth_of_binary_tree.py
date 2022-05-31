from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # BFS, TC = O(n), SC = O(n)
        max_depth = float('inf')
        deq = deque()
        if root:
            deq.append([root, 1])
        else:
            return 0

        while deq:
            node, level = deq.popleft()
            if node.left:
                deq.append([node.left, level + 1])
            if node.right:
                deq.append([node.right, level + 1])
            if not node.left and not node.right:
                max_depth = min(max_depth, level)

        return max_depth

    def minDepth2(self, root: Optional[TreeNode]) -> int:
        # DFS, TC = O(n), SC = O(n)
        self.min_depth = float('inf')

        def dfs(node, level=1):
            if node.left:
                dfs(node.left, level + 1)
            if node.right:
                dfs(node.right, level + 1)
            if not node.left and not node.right:
                self.min_depth = min(self.min_depth, level)

        if root:
            dfs(root)
            return self.min_depth
        else:
            return 0


if __name__ == '__main__':
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)

    solution = Solution()
    result = solution.minDepth(root)
    print(result)
    result = solution.minDepth2(root)
    print(result)
