from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidSequence(self, root: Optional[TreeNode], arr: List[int]) -> bool:
        def dfs(node, depth=0):
            if not node or depth == len(arr) or arr[depth] != node.val:
                return False
            if not node.left and not node.right and depth + 1 == len(arr):
                return True
            return any([dfs(node.left, depth + 1),
                        dfs(node.right, depth + 1)])
        return dfs(root)


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.right = TreeNode(2)
    arr = [1, 2]
    result = solution.isValidSequence(root, arr)
    print(result)
