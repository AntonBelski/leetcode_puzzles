from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs_tree(node, low, high):
            if not node:
                return

            if low <= node.val <= high:
                self.result += node.val
            if node.val > low:
                dfs_tree(node.left, low, high)
            if node.val < high:
                dfs_tree(node.right, low, high)

        self.result = 0
        dfs_tree(root, low, high)

        return self.result


if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    solution = Solution()
    low = 3
    high = 5
    result = solution.rangeSumBST(root, low, high)
    print(result)
