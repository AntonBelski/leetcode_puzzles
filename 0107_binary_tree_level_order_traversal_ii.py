from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        deq = deque()
        if root:
            deq.append([root, 0])
        while deq:
            node, level = deq.popleft()
            if level == len(result):
                result.append([])
            result[level].append(node.val)
            if node.left:
                deq.append([node.left, level + 1])
            if node.right:
                deq.append([node.right, level + 1])

        return result[::-1]


if __name__ == '__main__':
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)

    solution = Solution()
    result = solution.levelOrderBottom(root)
    print(result)
