from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.cams = 0

        def dfs(node):
            if not node:
                return -1
            l_choice = dfs(node.left)
            r_choice = dfs(node.right)
            choice = max(l_choice, r_choice)
            if choice == 2:
                self.cams += 1
                choice = 0
            elif choice == -1 or 0 not in [l_choice, r_choice]:
                choice = 2
            else:
                choice = 1
            return choice

        root_choice = dfs(root)
        if self.cams == 0 or root_choice >= 2:
            self.cams += 1
        return self.cams


if __name__ == '__main__':
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)

    solution = Solution()
    result = solution.minCameraCover(root)
    print(result)
