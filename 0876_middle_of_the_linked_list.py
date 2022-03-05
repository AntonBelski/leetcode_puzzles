from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow


if __name__ == '__main__':
    solution = Solution()
    list_node_fifth = ListNode(val=5)
    list_node_fourth = ListNode(val=4, next=list_node_fifth)
    list_node_third = ListNode(val=3, next=list_node_fourth)
    list_node_second = ListNode(val=2, next=list_node_third)
    list_node_first = ListNode(val=1, next=list_node_second)
    middle_node = solution.middleNode(list_node_first)
    print(f'Head, value = {middle_node.val}, next node value = {middle_node.next.val}')
