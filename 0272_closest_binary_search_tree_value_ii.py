from heapq import heappush, heappop
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        self.target = target
        self.k = k
        self.heap = []

        def traverse_tree(node):
            if not node:
                return

            dist = abs(self.target - node.val)
            heappush(self.heap, [-dist, node.val])
            if len(self.heap) > self.k:
                heappop(self.heap)

            traverse_tree(node.left)
            traverse_tree(node.right)

        traverse_tree(root)
        return [pair[1] for pair in self.heap]


if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    solution = Solution()
    target = 3.234234
    k = 2
    result = solution.closestKValues(root, target, k)
    print(result)
