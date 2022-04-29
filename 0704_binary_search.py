from typing import List


class Solution:
    def search2(self, arr: List[int], x: int) -> int:
        # Iterative solution, TC - O(log(n))
        lo, hi = 0, len(arr)

        while lo != hi:
            mid = (lo + hi) // 2
            if x <= arr[mid]:
                hi = mid
            else:
                lo = mid + 1

        if lo < len(arr) and arr[lo] == x:
            return lo
        else:
            return -1

    def search(self, arr, x, lo=0, hi=None):
        # Recursive solution, TC - O(log(n))
        if not hi:
            hi = len(arr)
        elif lo == hi:
            if lo < len(arr) and arr[lo] == x:
                return lo
            else:
                return -1

        mid = (lo + hi) // 2
        if x <= arr[mid]:
            return self.search(arr, x, lo, mid)
        else:
            return self.search(arr, x, mid + 1, hi)


if __name__ == '__main__':
    solution = Solution()
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    result = solution.search(nums, target)
    print(result)
    result = solution.search2(nums, target)
    print(result)
