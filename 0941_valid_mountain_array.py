from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        start = 0
        end = len(arr) - 1
        while start < len(arr) - 1 and arr[start] < arr[start + 1]:
            start += 1

        while end > 0 and arr[end - 1] > arr[end]:
            end -= 1

        if start == end and 0 < end < len(arr) - 1:
            return True
        else:
            return False


if __name__ == '__main__':
    solution = Solution()
    arr = [0, 3, 2, 1]
    result = solution.validMountainArray(arr)
    print(result)
