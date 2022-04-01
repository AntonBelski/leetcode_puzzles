from typing import List
from collections import Counter
from heapq import heapify, heappop


class Solution:
    def frequencySort(self, s: str) -> str:
        result = []
        s_freq = Counter(s)

        freq_pairs = [(-freq, ch) for ch, freq in s_freq.items()]
        heapify(freq_pairs)

        while freq_pairs:
            freq, ch = heappop(freq_pairs)
            result.append(-freq * ch)

        return ''.join(result)


if __name__ == '__main__':
    solution = Solution()
    s = "tree"
    result = solution.frequencySort(s)
    print(result)
