from typing import List


class Solution:
    def binaryGap(self, n: int) -> int:
        bin_n = bin(n)[2:]
        start = bin_n.find('1')
        max_seq = 0

        if start == -1:
            return max_seq

        curr_seq = 1
        for i in range(start + 1, len(bin_n)):
            if bin_n[i] == '0':
                curr_seq += 1
            else:
                max_seq = max(max_seq, curr_seq)
                curr_seq = 1

        return max_seq


if __name__ == '__main__':
    solution = Solution()
    n = 22
    result = solution.binaryGap(n)
    print(result)
