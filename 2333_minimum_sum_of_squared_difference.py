from collections import defaultdict
from typing import List


class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        diff = defaultdict(int)
        for i in range(len(nums1)):
            diff[abs(nums1[i] - nums2[i])] += 1
        biggest = max(diff)
        changes = k1 + k2
        while biggest != 0 and changes > 0:
            count = diff[biggest]
            if count <= changes:
                del diff[biggest]
                biggest -= 1
                diff[biggest] += count
                changes -= count
            else:
                diff[biggest] -= changes
                diff[biggest - 1] += changes
                break
        return sum([(num ** 2) * freq for num, freq in diff.items()])


if __name__ == '__main__':
    solution = Solution()
    nums1 = [1, 2, 3, 4]
    nums2 = [2, 10, 20, 19]
    k1 = 0
    k2 = 0
    result = solution.minSumSquareDiff(nums1, nums2, k1, k2)
    print(result)
