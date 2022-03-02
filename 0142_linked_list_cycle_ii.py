from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                cycle_len = self.get_cycle_len(slow)
                head_ahead = head

                for i in range(cycle_len):
                    head_ahead = head_ahead.next

                while head != head_ahead:
                    head = head.next
                    head_ahead = head_ahead.next

                return head

    def get_cycle_len(self, slow):
        cycle_len = 1
        cycle_pointer = slow.next

        while cycle_pointer != slow:
            cycle_pointer = cycle_pointer.next
            cycle_len += 1

        return cycle_len


if __name__ == '__main__':
    solution = Solution()
    list_node_fifth = ListNode(val=5)
    list_node_fourth = ListNode(val=4, next=list_node_fifth)
    list_node_third = ListNode(val=3, next=list_node_fourth)
    list_node_second = ListNode(val=2, next=list_node_third)
    list_node_first = ListNode(val=1, next=list_node_second)
    print(solution.detectCycle(list_node_first))
    list_node_fifth.next = list_node_third
    cycle_head = solution.detectCycle(list_node_first)
    print(f'Cycle head, value = {cycle_head.val}, next node value = {cycle_head.next.val}')
