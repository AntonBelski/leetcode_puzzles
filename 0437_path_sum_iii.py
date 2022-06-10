from collections import defaultdict
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = None


class Solution:
    def pathSum(self, root: Optional[TreeNode], target: int) -> int:
        def dfs(node, paths, path=0):
            if not node:
                return 0
            path += node.val
            result = paths[path - target]
            paths[path] += 1
            result += dfs(node.left, paths, path) + dfs(node.right, paths, path)
            paths[path] -= 1
            return result

        paths = defaultdict(int)
        paths[0] = 1
        return dfs(root, paths)


if __name__ == '__main__':
    root = TreeNode(2)
    root.left = TreeNode(-1)
    root.right = TreeNode(1)
    root.left.left = TreeNode(0)
    root.right.left = TreeNode(-1)
    root.right.right = TreeNode(1)

    solution = Solution()
    target = 2
    result = solution.pathSum(root, target)
    print(result)
