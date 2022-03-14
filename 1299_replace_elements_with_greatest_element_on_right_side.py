from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        last = -1

        for i in range(len(arr) - 1, -1, -1):
            last, arr[i] = max(arr[i], last), last

        return arr


if __name__ == '__main__':
    solution = Solution()
    arr = [17, 18, 5, 4, 6, 1]
    result = solution.replaceElements(arr)
    print(result)
