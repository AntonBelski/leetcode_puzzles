from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = None


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        deq = deque()
        result = []
        if root:
            deq.append([root, 0])

        while deq:
            node, level = deq.popleft()
            if node.left:
                deq.append([node.left, level + 1])
            if node.right:
                deq.append([node.right, level + 1])
            if deq and level != deq[0][1]:
                result.append(node.val)
        if root:
            result.append(node.val)

        return result


if __name__ == '__main__':
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)

    solution = Solution()
    result = solution.rightSideView(root)
    print(result)
