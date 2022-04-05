from typing import List
from collections import Counter


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        arr_counter = Counter(arr)
        result = len(arr_counter)
        freq_counter = Counter(arr_counter.values())

        for freq in range(1, len(arr) + 1):
            if k == 0:
                break
            elif freq_counter[freq] * freq <= k:
                k -= freq_counter[freq] * freq
                result -= freq_counter[freq]
            else:
                result -= k // freq
                break

        return result


if __name__ == '__main__':
    solution = Solution()
    arr = [4, 3, 1, 1, 3, 3, 2]
    k = 3
    result = solution.findLeastNumOfUniqueInts(arr, k)
    print(result)
