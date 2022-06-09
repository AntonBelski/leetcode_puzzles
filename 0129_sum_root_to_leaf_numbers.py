from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.result = 0

        def dfs(node, path=0):
            if not node:
                return
            curr_path = path * 10 + node.val
            if not node.left and not node.right:
                self.result += curr_path
            dfs(node.left, curr_path)
            dfs(node.right, curr_path)

        dfs(root)
        return self.result


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.right = TreeNode(2)
    result = solution.sumNumbers(root)
    print(result)
