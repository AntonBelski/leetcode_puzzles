from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, minimum=-float('inf'), maximum=float('inf')):
            if not node:
                return True
            return all([minimum < node.val < maximum,
                        dfs(node.left, minimum, node.val),
                        dfs(node.right, node.val, maximum)])
        return dfs(root)


if __name__ == '__main__':
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    solution = Solution()
    result = solution.isValidBST(root)
    print(result)
