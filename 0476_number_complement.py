from typing import List


class Solution:
    def findComplement(self, num: int) -> int:
        mask = num
        mask |= mask >> 1
        mask |= mask >> 2
        mask |= mask >> 4
        mask |= mask >> 8
        mask |= mask >> 16

        return mask ^ num


if __name__ == '__main__':
    solution = Solution()
    num = 5
    result = solution.findComplement(num)
    print(result)
