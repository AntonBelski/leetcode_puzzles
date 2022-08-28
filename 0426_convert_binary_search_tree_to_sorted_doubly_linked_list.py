from typing import List, Optional


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        self.head = self.pred = None

        def dfs_tree(node):
            if not node:
                return None

            dfs_tree(node.left)
            if self.pred:
                self.pred.right = node
                node.left = self.pred
                self.pred = node
            else:
                self.pred = self.head = node
            dfs_tree(node.right)

        dfs_tree(root)
        if self.head:
            self.pred.right = self.head
            self.head.left = self.pred

        return self.head


if __name__ == '__main__':
    root = Node(4)
    root.left = Node(2)
    root.right = Node(5)
    root.left.left = Node(1)
    root.left.right = Node(3)
    solution = Solution()
    head = solution.treeToDoublyList(root)
    node = head
    while node.right != head:
        print(node.val)
        node = node.right
    print(node.val)
