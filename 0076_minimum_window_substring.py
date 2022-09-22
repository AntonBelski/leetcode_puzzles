from collections import Counter, defaultdict
from typing import List


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter_t, window = Counter(t), defaultdict(int)
        start = balance = 0
        res = [len(s), 2 * len(s)]

        for i, ch in enumerate(s):
            if ch in counter_t:
                window[ch] += 1
                if window[ch] <= counter_t[ch]:
                    balance += 1
                if balance < len(t):
                    continue
                while s[start] not in counter_t or window[s[start]] > counter_t[s[start]]:
                    if s[start] in counter_t:
                        window[s[start]] -= 1
                    start += 1
                if i + 1 - start <= res[1] - res[0]:
                    res = [start, i + 1]

        return s[res[0]:res[1]]


if __name__ == '__main__':
    solution = Solution()
    s = "ADOBECODEBANC"
    t = "ABC"
    result = solution.minWindow(s, t)
    print(result)
