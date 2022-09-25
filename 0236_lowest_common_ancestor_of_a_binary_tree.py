class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.p, self.q = p, q
        self.p_path, self.q_path = [], []

        def dfs(node, curr_path):
            if not node:
                return
            curr_path.append(node)

            if node == self.p:
                self.p_path = curr_path[:]
            if node == self.q:
                self.q_path = curr_path[:]
            if self.p_path and self.q_path:
                return

            dfs(node.left, curr_path)
            dfs(node.right, curr_path)

            curr_path.pop()

        dfs(root, [])
        min_len = min(len(self.p_path), len(self.q_path))
        i = 0

        while i + 1 < min_len and self.q_path[i + 1] == self.p_path[i + 1]:
            i += 1

        return self.p_path[i]


if __name__ == '__main__':
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)

    node_p = root.right.right
    node_q = root.right.left

    solution = Solution()
    result = solution.lowestCommonAncestor(root, node_p, node_q)
    print(result.val)
