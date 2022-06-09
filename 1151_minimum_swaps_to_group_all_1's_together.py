from collections import Counter
from typing import List


class Solution:
    def minSwaps(self, data: List[int]) -> int:
        ones_count = sum(data)
        curr_ones = 0

        if ones_count < 2:
            return 0

        for i in range(ones_count):
            curr_ones += data[i]
        result = curr_ones

        for i in range(ones_count, len(data)):
            curr_ones += data[i]
            curr_ones -= data[i - ones_count]
            result = max(result, curr_ones)

        return ones_count - result


if __name__ == '__main__':
    solution = Solution()
    data = [1, 0, 1, 0, 1]
    result = solution.minSwaps(data)
    print(result)
