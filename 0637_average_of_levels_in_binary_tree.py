from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # BFS, TC = O(n), SC = O(n)
        result = []
        prev_level = -1
        deq = deque()
        deq.append([root, 0])

        while deq:
            node, level = deq.popleft()
            if level != prev_level:
                if prev_level >= 0:
                    result.append(level_sum / count)
                level_sum, count = node.val, 1
            else:
                level_sum += node.val
                count += 1
            prev_level = level

            if node.left:
                deq.append([node.left, level + 1])
            if node.right:
                deq.append([node.right, level + 1])

        result.append(level_sum / count)
        return result

    def averageOfLevels2(self, root: Optional[TreeNode]) -> List[float]:
        # DFS Pre-order, TC = O(n), SC = O(n)
        result = []
        averages = []

        def dfs_inorder(node, level=0):
            if level == len(averages):
                averages.append([0, 0])
            averages[level][0] += node.val
            averages[level][1] += 1
            if node.left:
                dfs_inorder(node.left, level + 1)
            if node.right:
                dfs_inorder(node.right, level + 1)

        dfs_inorder(root)

        for pair in averages:
            result.append(pair[0] / pair[1])

        return result


if __name__ == '__main__':
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)

    solution = Solution()
    result = solution.averageOfLevels(root)
    print(result)
    result = solution.averageOfLevels2(root)
    print(result)
