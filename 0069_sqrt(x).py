from typing import List


class Solution:
    def mySqrt(self, x: int) -> int:
        lo, hi = 0, x + 1
        while lo != hi:
            mid = (lo + hi) // 2
            if mid * mid > x:
                hi = mid
            else:
                lo = mid + 1
        return lo - 1


if __name__ == '__main__':
    solution = Solution()
    result = solution.mySqrt(4)
    print(result)
