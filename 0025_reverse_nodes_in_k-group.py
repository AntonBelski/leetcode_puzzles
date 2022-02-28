from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head.next or k == 1:
            return head

        list_len = 1
        node = head
        while node.next:
            node = node.next
            list_len += 1

        pre_head = ListNode(next=head)
        result_head = None
        start = 0
        while start + k <= list_len:
            prev_node = None
            node = pre_head.next
            next_node = node.next
            node.next = prev_node

            for i in range(k - 1):
                prev_node = node
                node = next_node
                next_node = node.next
                node.next = prev_node

            start += k
            pre_head.next.next = next_node
            new_head = pre_head.next
            pre_head.next = node
            pre_head = new_head

            if not result_head:
                result_head = node

        return result_head if result_head else head


if __name__ == '__main__':
    solution = Solution()
    list_node_fifth = ListNode(val=5)
    list_node_fourth = ListNode(val=4, next=list_node_fifth)
    list_node_third = ListNode(val=3, next=list_node_fourth)
    list_node_second = ListNode(val=2, next=list_node_third)
    list_node_first = ListNode(val=1, next=list_node_second)
    k = 2
    new_head = solution.reverseKGroup(list_node_first, k)
    print(f'Head, value = {new_head.val}, next node value = {new_head.next.val}')
    next_node = new_head.next
    print(f'Second node, value = {next_node.val}, next node value = {next_node.next.val}')
    next_node = next_node.next
    print(f'Third node, value = {next_node.val}, next node value = {next_node.next.val}')
    next_node = next_node.next
    print(f'Fourth node, value = {next_node.val}, next node value = {next_node.next.val}')
    next_node = next_node.next
    print(f'Fifth node, value = {next_node.val}, next node = {next_node.next}')
