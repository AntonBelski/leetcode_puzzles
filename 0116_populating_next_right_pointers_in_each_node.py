from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = None

    def print_level_order(self):
        next_level_root = self
        while next_level_root:
            current = next_level_root
            next_level_root = None
            while current:
                print(str(current.val) + " ", end='')
                if not next_level_root:
                    if current.left:
                        next_level_root = current.left
                    elif current.right:
                        next_level_root = current.right
                current = current.next
            print()


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # BFS, TC = O(n), SC = O(n)
        deq = deque()
        if root:
            deq.append([root, 0])

        while deq:
            node, level = deq.popleft()
            if node.left:
                deq.append([node.left, level + 1])
            if node.right:
                deq.append([node.right, level + 1])
            if deq and level == deq[0][1]:
                node.next = deq[0][0]

        return root




if __name__ == '__main__':
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)

    solution = Solution()
    root = solution.connect(root)
    root.print_level_order()
