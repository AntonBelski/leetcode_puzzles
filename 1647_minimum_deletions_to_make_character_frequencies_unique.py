from collections import Counter
from typing import List


class Solution:
    def minDeletions(self, s: str) -> int:
        freqs = Counter(s).values()
        counter = Counter(freqs)
        freqs = sorted(freqs)[::-1]
        result = 0

        for freq in freqs:
            if counter[freq] == 1:
                continue
            curr_freq = freq
            while counter[curr_freq] > 0 and curr_freq > 0:
                curr_freq -= 1
                result += 1
            counter[curr_freq] += 1
            counter[freq] -= 1

        return result


if __name__ == '__main__':
    solution = Solution()
    s = "aaabbbcc"
    result = solution.minDeletions(s)
    print(result)
