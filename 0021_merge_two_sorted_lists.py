from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node = dummy_root = ListNode()
        while list1 or list2:
            if not list2:
                node.next = ListNode(list1.val)
                list1 = list1.next
            elif not list1 or list2.val < list1.val:
                node.next = ListNode(list2.val)
                list2 = list2.next
            else:
                node.next = ListNode(list1.val)
                list1 = list1.next
            node = node.next
        return dummy_root.next


if __name__ == '__main__':
    solution = Solution()
    list_node_fifth = ListNode(val=5)
    list_node_fourth = ListNode(val=4, next=list_node_fifth)
    list_node_third = ListNode(val=3, next=list_node_fourth)
    list_node_second = ListNode(val=2, next=list_node_third)
    list_node_first = ListNode(val=1, next=list_node_second)
    final_list_head = solution.mergeTwoLists(list_node_first, list_node_first)
    while final_list_head:
        print(final_list_head.val)
        final_list_head = final_list_head.next
