from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node.left:
                return bool(node.val)
            childs = [dfs(node.left), dfs(node.right)]
            if node.val == 2:
                return any(childs)
            else:
                return all(childs)

        return dfs(root)


if __name__ == '__main__':
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(1)
    solution = Solution()
    result = solution.evaluateTree(root)
    print(result)
