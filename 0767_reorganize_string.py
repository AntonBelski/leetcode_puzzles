from typing import List
from collections import Counter
from heapq import heapify, heappop, heappush


class Solution:
    def reorganizeString(self, s: str) -> str:
        s_freq = Counter(s)
        heap = [[-freq, ch] for ch, freq in s_freq.items()]
        heapify(heap)
        result = []

        while len(heap) > 1:
            first_top = heappop(heap)
            second_top = heappop(heap)

            if not result or result[-1] != first_top[1]:
                result.append(first_top[1])
                first_top[0] += 1

            result.append(second_top[1])
            second_top[0] += 1

            if second_top[0] != 0:
                heappush(heap, second_top)
            if first_top[0] != 0:
                heappush(heap, first_top)

        if heap:
            if heap[0][0] != -1 or (result and result[-1] == heap[0][1]):
                return ''
            result.append(heap[0][1])

        return ''.join(result)


if __name__ == '__main__':
    solution = Solution()
    s = "aab"
    result = solution.reorganizeString(s)
    print(result)
