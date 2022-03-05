from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev, curr = None, slow
        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        start_node = head
        end_node = prev

        while start_node.next:
            next_node = start_node.next
            start_node.next = end_node
            start_node = next_node
            if end_node.next:
                next_node = end_node.next
                end_node.next = start_node
                end_node = next_node


if __name__ == '__main__':
    solution = Solution()
    list_node_fifth = ListNode(val=1)
    list_node_fourth = ListNode(val=2, next=list_node_fifth)
    list_node_third = ListNode(val=3, next=list_node_fourth)
    list_node_second = ListNode(val=4, next=list_node_third)
    list_node_first = ListNode(val=5, next=list_node_second)
    solution.reorderList(list_node_first)
    print(f'Head, value = {list_node_first.val}, next node value = {list_node_first.next.val}')
    next_node = list_node_first.next
    print(f'Second node, value = {next_node.val}, next node value = {next_node.next.val}')
    next_node = next_node.next
    print(f'Third node, value = {next_node.val}, next node value = {next_node.next.val}')
    next_node = next_node.next
    print(f'Fourth node, value = {next_node.val}, next node value = {next_node.next.val}')
    next_node = next_node.next
    print(f'Fifth node, value = {next_node.val}, next node = {next_node.next}')
