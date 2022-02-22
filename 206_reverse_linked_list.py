from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or head.next is None:
            return head

        prev_node = None
        node = head
        next_node = node.next
        node.next = prev_node

        while next_node:
            prev_node = node
            node = next_node
            next_node = node.next
            node.next = prev_node

        return node


if __name__ == '__main__':
    solution = Solution()
    list_node_fifth = ListNode(val=5)
    list_node_fourth = ListNode(val=4, next=list_node_fifth)
    list_node_third = ListNode(val=3, next=list_node_fourth)
    list_node_second = ListNode(val=2, next=list_node_third)
    list_node_first = ListNode(val=1, next=list_node_second)
    new_head = solution.reverseList(list_node_first)
    print(f'Head, value = {new_head.val}, next node value = {new_head.next.val}')
    next_node = new_head.next
    print(f'Second node, value = {next_node.val}, next node value = {next_node.next.val}')
    next_node = next_node.next
    print(f'Third node, value = {next_node.val}, next node value = {next_node.next.val}')
    next_node = next_node.next
    print(f'Fourth node, value = {next_node.val}, next node value = {next_node.next.val}')
    next_node = next_node.next
    print(f'Fifth node, value = {next_node.val}, next node = {next_node.next}')
