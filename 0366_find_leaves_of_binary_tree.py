from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        def dfs(node, result):
            if not node:
                return 0
            left_ind = dfs(node.left, result)
            right_ind = dfs(node.right, result)
            ind = max(left_ind, right_ind)
            if ind == len(result):
                result.append([])
            result[ind].append(node.val)
            return ind + 1

        result = []
        dfs(root, result)
        return result


if __name__ == '__main__':
    root = TreeNode(7)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)

    solution = Solution()
    result = solution.findLeaves(root)
    print(result)
