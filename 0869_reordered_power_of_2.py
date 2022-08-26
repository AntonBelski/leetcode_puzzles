from collections import Counter
from typing import List


class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        str_n = str(n)
        boundary = 10 ** len(str_n)
        counter_n = Counter(str_n)
        num = 1

        while num < boundary // 10:
            num *= 2

        while num < boundary:
            if Counter(str(num)) == counter_n:
                return True
            num *= 2

        return False


if __name__ == '__main__':
    solution = Solution()
    n = 821
    result = solution.reorderedPowerOf2(n)
    print(result)
