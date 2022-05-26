from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder2(self, root: Optional[TreeNode]) -> List[List[int]]:
        # DFS Solution, Time Complexity - O(n), Space Complexity - O(n)
        return self.recursive_dfs(root, [])

    def recursive_dfs(self, node, result, depth=0):
        if node is not None:
            if depth >= len(result):
                result.append([])
            result[depth].append(node.val)
            self.recursive_dfs(node.left, result, depth + 1)
            self.recursive_dfs(node.right, result, depth + 1)
        return result

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # BFS Solution, Time Complexity - O(n), Space Complexity - O(n)
        deq = deque()
        result = []
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

        return result


if __name__ == '__main__':
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)

    solution = Solution()
    result = solution.levelOrder(root)
    print(result)
    result = solution.levelOrder2(root)
    print(result)
