class ArrayReader:
    def __init__(self, arr):
        self.arr = arr

    def get(self, index):
        if index >= len(self.arr):
            return float('inf')
        return self.arr[index]


class Solution:
    def binary_search(self, arr, x):
        lo, hi = 0, len(arr)
        while lo != hi:
            mid = (lo + hi) // 2
            if x <= arr[mid]:
                hi = mid
            else:
                lo = mid + 1
        return lo

    def search(self, reader: 'ArrayReader', x: int) -> int:
        lo, hi = 0, 10000
        while lo != hi:
            mid = (lo + hi) // 2
            if x <= reader.get(mid):
                hi = mid
            else:
                lo = mid + 1

        if reader.get(lo) == x:
            return lo
        else:
            return -1


if __name__ == '__main__':
    solution = Solution()
    reader = ArrayReader([4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])
    print(solution.search(reader, 16))
    print(solution.search(reader, 11))
    reader = ArrayReader([1, 3, 8, 10, 15])
    print(solution.search(reader, 15))
    print(solution.search(reader, 20))
