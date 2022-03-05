from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head.next:
            return True

        slow = head
        fast = head
        is_palindrome = True

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        last_node = self.reverse_list(slow)
        start_node = head
        end_node = last_node

        while end_node:
            if start_node.val != end_node.val:
                is_palindrome = False
                break
            start_node = start_node.next
            end_node = end_node.next

        self.reverse_list(last_node)
        return is_palindrome

    def reverse_list(self, node):
        prev_node = None
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
    list_node_fifth = ListNode(val=1)
    list_node_fourth = ListNode(val=2, next=list_node_fifth)
    list_node_third = ListNode(val=3, next=list_node_fourth)
    list_node_second = ListNode(val=2, next=list_node_third)
    list_node_first = ListNode(val=1, next=list_node_second)
    print(solution.isPalindrome(list_node_first))
