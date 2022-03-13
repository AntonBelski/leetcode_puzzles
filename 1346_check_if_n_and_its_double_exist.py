from typing import List
from collections import Counter


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr_dict = Counter(arr)

        for first in arr_dict:
            if first == 0 and arr_dict[first] > 1:
                return True
            elif first != 0 and arr_dict.get(first * 2):
                return True

        return False


if __name__ == '__main__':
    solution = Solution()
    arr = [10, 2, 5, 3]
    result = solution.checkIfExist(arr)
    print(result)
