from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        list_len = 1
        tail = head

        while tail.next:
            tail = tail.next
            list_len += 1

        if not k % list_len:
            return head

        end = list_len - k % list_len
        start = 1
        node = head

        while start != end:
            node = node.next
            start += 1

        new_head = node.next
        node.next = None
        tail.next = head

        return new_head


if __name__ == '__main__':
    solution = Solution()
    list_node_fifth = ListNode(val=5)
    list_node_fourth = ListNode(val=4, next=list_node_fifth)
    list_node_third = ListNode(val=3, next=list_node_fourth)
    list_node_second = ListNode(val=2, next=list_node_third)
    list_node_first = ListNode(val=1, next=list_node_second)
    k = 2
    new_head = solution.rotateRight(list_node_first, k)
    print(f'Head, value = {new_head.val}, next node value = {new_head.next.val}')
    next_node = new_head.next
    print(f'Second node, value = {next_node.val}, next node value = {next_node.next.val}')
    next_node = next_node.next
    print(f'Third node, value = {next_node.val}, next node value = {next_node.next.val}')
    next_node = next_node.next
    print(f'Fourth node, value = {next_node.val}, next node value = {next_node.next.val}')
    next_node = next_node.next
    print(f'Fifth node, value = {next_node.val}, next node = {next_node.next}')
