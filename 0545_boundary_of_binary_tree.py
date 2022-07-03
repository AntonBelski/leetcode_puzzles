from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = None


class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        left_boundary = []
        right_boundary = []
        leaves = []

        def dfs_boundary(node, boundary, is_right=1):
            boundary.append(node.val)
            childs = [node.left, node.right][::is_right]
            for child in childs:
                if child:
                    dfs_boundary(child, boundary, is_right)
                    break

        def dfs_leaves(node, leaves):
            if not node or not node.left and not node.right:
                if node:
                    leaves.append(node.val)
                return
            dfs_leaves(node.left, leaves)
            dfs_leaves(node.right, leaves)

        if root.left or root.right:
            left_boundary.append(root.val)
        if root.left:
            dfs_boundary(root.left, left_boundary)
            left_boundary.pop()
        if root.right:
            dfs_boundary(root.right, right_boundary, is_right=-1)
            right_boundary.pop()
            right_boundary.reverse()

        dfs_leaves(root, leaves)
        return left_boundary + leaves + right_boundary


if __name__ == '__main__':
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)

    solution = Solution()
    result = solution.boundaryOfBinaryTree(root)
    print(result)
