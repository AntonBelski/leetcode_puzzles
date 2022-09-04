from bisect import bisect_left
from random import randint
from typing import List


class Solution:
    def __init__(self, w: List[int]):
        self.ranges = [w[0]]
        self.w_sum = w[0]

        for i in range(1, len(w)):
            self.ranges.append(self.ranges[-1] + w[i])
            self.w_sum += w[i]

    def pickIndex(self) -> int:
        rand_val = randint(1, self.w_sum)
        choice = bisect_left(self.ranges, rand_val)
        return choice

    def pickIndex2(self) -> int:
        rand_val = randint(1, self.w_sum)
        lo, hi = 0, len(self.ranges) - 1

        while lo != hi:
            mid = (lo + hi) // 2
            if rand_val <= self.ranges[mid]:
                hi = mid
            else:
                lo = mid + 1
        return lo


if __name__ == '__main__':
    w = [1, 3]
    solution = Solution(w)
    print(solution.pickIndex())
    print(solution.pickIndex())
    print(solution.pickIndex())
    print(solution.pickIndex())
    print(solution.pickIndex())
    print()

    print(solution.pickIndex2())
    print(solution.pickIndex2())
    print(solution.pickIndex2())
    print(solution.pickIndex2())
    print(solution.pickIndex2())
