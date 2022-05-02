class MountainArray:
    def __init__(self, arr):
        self.arr = arr

    def get(self, index: int) -> int:
        return self.arr[index]

    def length(self) -> int:
        return len(self.arr)


class Solution:
    def binary_search_max(self, arr):
        lo, hi = 0, arr.length() - 1
        while lo != hi:
            mid = (lo + hi) // 2
            if arr.get(mid) > arr.get(mid + 1):
                hi = mid
            else:
                lo = mid + 1
        return lo

    def binary_search(self, arr, max_elem_ind, x, is_ascending=True):
        if is_ascending:
            lo, hi = 0, max_elem_ind
        else:
            lo, hi = max_elem_ind, arr.length() - 1

        while lo != hi:
            mid = (lo + hi) // 2
            if x <= arr.get(mid) if is_ascending else x >= arr.get(mid):
                hi = mid
            else:
                lo = mid + 1

        return lo

    def findInMountainArray(self, x: int, arr: 'MountainArray') -> int:
        max_elem_ind = self.binary_search_max(arr)

        left_ind = self.binary_search(arr, max_elem_ind, x)
        if arr.get(left_ind) == x:
            return left_ind

        right_ind = self.binary_search(arr, max_elem_ind, x, is_ascending=False)
        if arr.get(right_ind) == x:
            return right_ind
        else:
            return -1


if __name__ == '__main__':
    solution = Solution()
    mountain_arr = MountainArray([1, 2, 3, 4, 5, 3, 1])
    result = solution.findInMountainArray(3, mountain_arr)
    print(result)
