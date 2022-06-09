from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], target: int) -> List[List[int]]:
        result = []
        curr_path = []

        def dfs(node, path_sum=0):
            if not node:
                return
            curr_path.append(node.val)
            if not node.left and not node.right:
                if path_sum + node.val == target:
                    result.append(curr_path[:])
            dfs(node.left, path_sum + node.val)
            dfs(node.right, path_sum + node.val)
            curr_path.pop()

        dfs(root)
        return result


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.right = TreeNode(2)
    targetSum = 4
    result = solution.pathSum(root, targetSum)
    print(result)
