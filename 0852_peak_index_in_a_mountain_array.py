from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        lo, hi = 0, len(arr) - 1
        while lo != hi:
            mid = (lo + hi) // 2
            if arr[mid] > arr[mid + 1]:
                hi = mid
            else:
                lo = mid + 1
        return lo


if __name__ == '__main__':
    solution = Solution()
    arr = [0, 2, 1, 0]
    result = solution.peakIndexInMountainArray(arr)
    print(result)
