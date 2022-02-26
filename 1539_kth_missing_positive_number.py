from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        arr_start = 0
        k_start = 0
        n = len(arr)
        for i in range(n + k):
            if arr_start < n and arr[arr_start] == i + 1:
                arr_start += 1
            else:
                k_start += 1

            if k_start == k:
                return i + 1


if __name__ == '__main__':
    solution = Solution()
    arr = [2, 3, 4, 7, 11]
    k = 5
    result = solution.findKthPositive(arr.copy(), k)
    print(result)
