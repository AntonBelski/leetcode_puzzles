from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def dfs(node, ind=0):
            if not node:
                return ind + 1
            left_ind = dfs(node.left, ind - 1)
            right_ind = dfs(node.right, ind + 1)
            return min(left_ind, right_ind)

        if not root:
            return []
        start_ind = abs(dfs(root))
        result = [[] for _ in range(start_ind)]
        deq = deque()
        deq.append([root, start_ind])
        while deq:
            node, ind = deq.popleft()
            if ind == len(result):
                result.append([])
            result[ind].append(node.val)
            if node.left:
                deq.append([node.left, ind - 1])
            if node.right:
                deq.append([node.right, ind + 1])

        return result


if __name__ == '__main__':
    root = TreeNode(7)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)

    solution = Solution()
    result = solution.verticalOrder(root)
    print(result)
