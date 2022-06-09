from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum2(self, root: Optional[TreeNode], target: int) -> bool:
        # DFS Recursive, TC = O(n), SC = O(n)
        def pre_order_dfs(node, path=0):
            if not node:
                return False
            elif not node.left and not node.right:
                return path + node.val == target
            else:
                return any([pre_order_dfs(node.left, path + node.val),
                            pre_order_dfs(node.right, path + node.val)])

        return pre_order_dfs(root)

    def hasPathSum(self, root: Optional[TreeNode], target: int) -> bool:
        # DFS Iterative, TC = O(n), SC = O(n)
        stack = []
        if root:
            stack.append([root, 0])

        while stack:
            node, path = stack.pop()
            if node.right:
                stack.append([node.right, path + node.val])
            if node.left:
                stack.append([node.left, path + node.val])
            if not node.left and not node.right:
                if path + node.val == target:
                    return True

        return False


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.right = TreeNode(2)
    targetSum = 4
    result = solution.hasPathSum2(root, targetSum)
    print(result)
    result = solution.hasPathSum(root, targetSum)
    print(result)
