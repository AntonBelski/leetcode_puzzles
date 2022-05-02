from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry_node = result_node = ListNode()
        prev_sum = 0

        while l1 or l2:
            curr_sum = prev_sum
            if l1:
                curr_sum += l1.val
                l1 = l1.next

            if l2:
                curr_sum += l2.val
                l2 = l2.next

            prev_sum = curr_sum // 10
            result_node.next = ListNode(curr_sum % 10)
            result_node = result_node.next

        if prev_sum:
            result_node.next = ListNode(prev_sum % 10)

        return carry_node.next


if __name__ == '__main__':
    solution = Solution()
    first_list_node_third = ListNode(val=3)
    first_list_node_second = ListNode(val=4, next=first_list_node_third)
    first_list_node_first = ListNode(val=2, next=first_list_node_second)
    second_list_node_third = ListNode(val=4)
    second_list_node_second = ListNode(val=6, next=second_list_node_third)
    second_list_node_first = ListNode(val=5, next=second_list_node_second)
    new_head = solution.addTwoNumbers(l1=first_list_node_first, l2=second_list_node_first)
    print(f'Head, value = {new_head.val}, next node value = {new_head.next.val}')
    next_node = new_head.next
    print(f'Second node, value = {next_node.val}, next node value = {next_node.next.val}')
    next_node = next_node.next
    print(f'Third node, value = {next_node.val}, next node = {next_node.next}')
