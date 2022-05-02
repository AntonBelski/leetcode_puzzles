from typing import List


class Solution:
    def findClosestElements2(self, arr: List[int], k: int, x: int) -> List[int]:
        # First solution with Two Pointers
        # Time Complexity - O(n - k), Space Complexity - O(1)
        start = 0
        end = len(arr) - 1

        while end + 1 - start != k:
            if abs(x - arr[start]) > abs(x - arr[end]):
                start += 1
            else:
                end -= 1

        return arr[start:end + 1]

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Second solution with Binary Search + Two Pointers
        # Time Complexity - O(k + log(n)), Space Complexity - O(1)
        lo, hi = 0, len(arr) - 1
        while lo != hi:
            mid = (lo + hi) // 2
            if x <= arr[mid]:
                hi = mid
            else:
                lo = mid + 1

        if lo > 0 and abs(arr[lo - 1] - x) <= abs(arr[lo] - x):
            lo -= 1

        start = end = lo
        while end + 1 - start != k:
            if start == 0:
                end += 1
            elif end == len(arr) - 1:
                start -= 1
            elif abs(arr[start - 1] - x) <= abs(arr[end + 1] - x):
                start -= 1
            else:
                end += 1

        return arr[start:end + 1]


if __name__ == '__main__':
    solution = Solution()
    arr = [1, 2, 3, 4, 5]
    k = 4
    x = 3
    result = solution.findClosestElements2(arr, k, x)
    print(result)
    result = solution.findClosestElements(arr, k, x)
    print(result)
