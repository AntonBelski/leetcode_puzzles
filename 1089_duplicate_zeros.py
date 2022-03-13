from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]):
        n = len(arr)
        start = end = -1

        while end < n - 1:
            start += 1
            end += 1
            if arr[start] == 0:
                end += 1

        if end == n:
            end -= 1
            arr[end] = 0
            end -= 1
            start -= 1

        while start != end:
            arr[end] = arr[start]
            end -= 1
            if arr[start] == 0:
                arr[end] = arr[start]
                end -= 1
            start -= 1


if __name__ == '__main__':
    solution = Solution()
    arr = [1, 0, 2, 3, 0, 4, 5, 0]
    solution.duplicateZeros(arr)
    print(arr)
