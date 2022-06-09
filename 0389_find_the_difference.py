from collections import Counter
from typing import List


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_counter = Counter(s)
        t_counter = Counter(t)
        for ch in t_counter:
            if s_counter[ch] < t_counter[ch]:
                return ch


if __name__ == '__main__':
    solution = Solution()
    s = "abcd"
    t = "abcde"
    result = solution.findTheDifference(s, t)
    print(result)
