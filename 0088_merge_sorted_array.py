from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        end = n + m - 1
        n1_end = m - 1
        n2_end = n - 1

        while end >= 0:
            if n1_end >= 0 and n2_end >= 0:
                if nums1[n1_end] > nums2[n2_end]:
                    nums1[end] = nums1[n1_end]
                    n1_end -= 1
                else:
                    nums1[end] = nums2[n2_end]
                    n2_end -= 1
            elif n1_end >= 0:
                nums1[end] = nums1[n1_end]
                n1_end -= 1
            elif n2_end >= 0:
                nums1[end] = nums2[n2_end]
                n2_end -= 1
            end -= 1


if __name__ == '__main__':
    solution = Solution()
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    solution.merge(nums1, m, nums2, n)
    print(nums1)
