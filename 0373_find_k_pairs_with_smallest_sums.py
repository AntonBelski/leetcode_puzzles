from typing import List
from heapq import heapify, heappop, heappush


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        result = []
        heap = []
        for i, val in enumerate(nums2):
            heap.append([nums1[0] + val, i, 0])
        heapify(heap)

        while heap and k:
            val, n2_i, n1_i = heappop(heap)
            if n1_i + 1 < len(nums1):
                new_val = nums1[n1_i + 1] + nums2[n2_i]
                heappush(heap, [new_val, n2_i, n1_i + 1])
            result.append([nums1[n1_i], nums2[n2_i]])
            k -= 1

        return result


if __name__ == '__main__':
    solution = Solution()
    nums1 = [1, 7, 11]
    nums2 = [2, 4, 6]
    k = 3
    result = solution.kSmallestPairs(nums1=nums1, nums2=nums2, k=k)
    print(result)
