from heapq import heapify, heappop, heappush
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        filter_lists = [l for l in lists if l]
        heap = [[l.val, i] for i, l in enumerate(filter_lists)]
        result = []

        heapify(heap)
        while heap:
            val, ind = heappop(heap)

            if filter_lists[ind].next:
                next_node = filter_lists[ind].next
                heappush(heap, [next_node.val, ind])
                filter_lists[ind] = next_node

            new_node = ListNode(val)
            result.append(new_node)
            if len(result) != 1:
                result[-2].next = result[-1]

        return result[0] if filter_lists else None


if __name__ == '__main__':
    solution = Solution()
    first_list_first = ListNode(5)
    first_list_second = ListNode(4, next=first_list_first)
    first_list_three = ListNode(1, next=first_list_second)
    second_list_first = ListNode(4)
    second_list_second = ListNode(3, next=second_list_first)
    second_list_three = ListNode(1, next=second_list_second)
    third_list_first = ListNode(6)
    third_list_second = ListNode(2, next=third_list_first)
    lists = [first_list_three, second_list_three, third_list_second, None]
    final_list_head = solution.mergeKLists(lists)
    while final_list_head:
        print(final_list_head.val)
        final_list_head = final_list_head.next
