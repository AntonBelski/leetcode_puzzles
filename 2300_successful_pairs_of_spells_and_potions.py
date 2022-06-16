from bisect import bisect_left
from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        result = []
        potions.sort()
        for sp in spells:
            val = success / sp
            point = bisect_left(potions, val)
            result.append(len(potions) - point)
        return result


if __name__ == '__main__':
    solution = Solution()
    spells = [5, 1, 3]
    potions = [1, 2, 3, 4, 5]
    success = 7
    result = solution.successfulPairs(spells, potions, success)
    print(result)
