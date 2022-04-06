from typing import List
from collections import Counter
from heapq import heapify, heappop, heappush


class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        s_counter = Counter(s)
        window = {}
        result = []

        if len(s_counter) < k:
            return ''
        elif k < 2:
            return s

        heap = [[-freq, ch] for ch, freq in s_counter.items()]
        heapify(heap)

        for _ in range(k):
            freq, ch = heappop(heap)
            result.append(ch)
            window[ch] = freq + 1

        for i in range(k, len(s)):
            ch = result[i - k]
            freq = window.pop(ch)
            if freq != 0:
                heappush(heap, [freq, ch])

            if not heap:
                return ''

            freq, ch = heappop(heap)
            result.append(ch)
            window[ch] = freq + 1

        return ''.join(result)


if __name__ == '__main__':
    solution = Solution()
    s = "aabbcc"
    k = 3
    result = solution.rearrangeString(s, k)
    print(result)
