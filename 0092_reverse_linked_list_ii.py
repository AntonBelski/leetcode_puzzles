from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        pre_left = ListNode(next=head)
        count = 1
        while count != left:
            pre_left = pre_left.next
            count += 1

        prev_node = None
        node = pre_left.next
        next_node = node.next
        node.next = prev_node
        count += 1

        while count <= right:
            prev_node = node
            node = next_node
            next_node = node.next
            node.next = prev_node
            count += 1

        pre_left.next.next = next_node
        pre_left.next = node

        return pre_left.next if left == 1 else head


if __name__ == '__main__':
    solution = Solution()
    list_node_fifth = ListNode(val=5)
    list_node_fourth = ListNode(val=4, next=list_node_fifth)
    list_node_third = ListNode(val=3, next=list_node_fourth)
    list_node_second = ListNode(val=2, next=list_node_third)
    list_node_first = ListNode(val=1, next=list_node_second)
    left = 2
    right = 4
    new_head = solution.reverseBetween(list_node_first, left, right)
    print(f'Head, value = {new_head.val}, next node value = {new_head.next.val}')
    next_node = new_head.next
    print(f'Second node, value = {next_node.val}, next node value = {next_node.next.val}')
    next_node = next_node.next
    print(f'Third node, value = {next_node.val}, next node value = {next_node.next.val}')
    next_node = next_node.next
    print(f'Fourth node, value = {next_node.val}, next node value = {next_node.next.val}')
    next_node = next_node.next
    print(f'Fifth node, value = {next_node.val}, next node = {next_node.next}')
