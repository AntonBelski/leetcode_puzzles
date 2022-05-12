from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        all_len = len(nums1) + len(nums2)
        left_size = (all_len + 1) // 2

        lo, hi = 0, len(nums1) - 1
        while True:
            med1 = (lo + hi) // 2
            med2 = left_size - 1 - (med1 + 1)

            left1 = -float('inf') if med1 < 0 else nums1[med1]
            right1 = float('inf') if med1 + 1 >= len(nums1) else nums1[med1 + 1]
            left2 = -float('inf') if med2 < 0 else nums2[med2]
            right2 = float('inf') if med2 + 1 >= len(nums2) else nums2[med2 + 1]

            if left1 > right2:
                hi = med1 if hi != 0 else med1 - 1
            elif left2 > right1:
                lo = med1 + 1
            else:
                break

        if all_len % 2 == 1:
            return max(left1, left2)
        else:
            return (max(left1, left2) + min(right1, right2)) / 2


if __name__ == '__main__':
    solution = Solution()
    nums1 = [1, 2]
    nums2 = [3, 4]
    result = solution.findMedianSortedArrays(nums1, nums2)
    print(result)
