from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]):
        def dfs(node):
            if not node:
                return 0, 0
            left_path, left_val = dfs(node.left)
            right_path, right_val = dfs(node.right)
            curr_path = 0
            max_path = 0
            if node.val == left_val:
                curr_path = max(curr_path, left_path)
                max_path += left_path
            if node.val == right_val:
                curr_path = max(curr_path, right_path)
                max_path += right_path
            self.max_path = max(self.max_path, max_path + 1)
            return curr_path + 1, node.val

        if not root:
            return 0
        self.max_path = -float('inf')
        dfs(root)
        return self.max_path - 1


if __name__ == '__main__':
    root = TreeNode(7)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)

    solution = Solution()
    result = solution.longestUnivaluePath(root)
    print(result)
