from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        start = 0
        end = len(arr) - 1

        while end + 1 - start != k:
            if abs(x - arr[start]) > abs(x - arr[end]):
                start += 1
            else:
                end -= 1

        return arr[start:end + 1]


if __name__ == '__main__':
    solution = Solution()
    arr = [1, 2, 3, 4, 5]
    k = 4
    x = 3
    result = solution.findClosestElements(arr, k, x)
    print(result)
