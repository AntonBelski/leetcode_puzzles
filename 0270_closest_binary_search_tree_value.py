from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        self.closest = root.val
        node = root

        while node:
            if abs(node.val - target) < abs(self.closest - target):
                self.closest = node.val
            if node.val > target:
                node = node.left
            else:
                node = node.right

        return self.closest


if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    solution = Solution()
    k = 3.234234
    result = solution.closestValue(root, k)
    print(result)
