from typing import List, Optional


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    def getIntersectionNode2(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # My Solution, Time Complexity - O(N + M), Space Complexity - O(1), best asymptotic, but code can be cleaner
        a_size, b_size = 1, 1
        a_tail, b_tail = headA, headB
        while a_tail.next or b_tail.next:
            if a_tail.next:
                a_tail = a_tail.next
                a_size += 1
            else:
                b_tail = b_tail.next
                b_size += 1

        if a_tail != b_tail:
            return None

        a_node, b_node = headA, headB
        for i in range(abs(a_size - b_size)):
            if a_size > b_size:
                a_node = a_node.next
            else:
                b_node = b_node.next

        while a_node != b_node:
            a_node = a_node.next
            b_node = b_node.next

        return a_node

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # Very Smart Solution, Time Complexity - O(N + M), Space Complexity - O(1), code is very clean
        node_a = headA
        node_b = headB

        while node_a != node_b:
            node_a = headB if not node_a else node_a.next
            node_b = headA if not node_b else node_b.next

        return node_a


if __name__ == '__main__':
    solution = Solution()
    first_list_node_third = ListNode(val=3)
    first_list_node_second = ListNode(val=4, next=first_list_node_third)
    first_list_node_first = ListNode(val=2, next=first_list_node_second)
    second_list_node_second = ListNode(val=4, next=first_list_node_third)
    second_list_node_first = ListNode(val=5, next=second_list_node_second)
    second_list_node_zero = ListNode(val=7, next=second_list_node_first)
    connections = [[1, 2, 5], [1, 3, 6], [2, 3, 1]]
    result = solution.getIntersectionNode(first_list_node_first, second_list_node_zero)
    print(result.val)
    result = solution.getIntersectionNode2(first_list_node_first, second_list_node_zero)
    print(result.val)
