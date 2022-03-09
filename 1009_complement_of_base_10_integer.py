from typing import List


class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1

        mask = n
        mask |= mask >> 1
        mask |= mask >> 2
        mask |= mask >> 4
        mask |= mask >> 8
        mask |= mask >> 16

        return mask ^ n


if __name__ == '__main__':
    solution = Solution()
    num = 5
    result = solution.bitwiseComplement(num)
    print(result)
