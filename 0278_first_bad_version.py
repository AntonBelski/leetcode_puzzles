from typing import List


class Solution:
    def __init__(self, bad_version):
        self.bad_version = bad_version

    def isBadVersion(self, v):
        return v >= self.bad_version

    def condition(self, mid):
        return self.isBadVersion(mid + 1)

    def firstBadVersion(self, n: int) -> int:
        lo, hi = 0, n
        while lo != hi:
            mid = (lo + hi) // 2
            if self.condition(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo + 1


if __name__ == '__main__':
    bad_version = 4
    solution = Solution(bad_version=bad_version)
    n = 5
    result = solution.firstBadVersion(n)
    print(result)
