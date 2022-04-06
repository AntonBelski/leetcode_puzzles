from typing import List
from collections import Counter
from heapq import heapify, heappop, heappush


class Solution:
    def leastInterval2(self, tasks: List[str], n: int) -> int:
        # Approach 1. Binary Heap + Hash Table + Sliding Window, TC - O(N*log(26)) ~ O(N), SC - O(26) ~ O(1)
        if n < 1:
            return len(tasks)

        n += 1
        tasks_counter = Counter(tasks)
        result = 0
        window = {}
        heap = [[-freq, ch] for ch, freq in tasks_counter.items()]
        heapify(heap)

        for i in range(n):
            if heap:
                freq, ch = heappop(heap)
                if freq + 1 != 0:
                    window[i] = [freq + 1, ch]
            elif not window:
                break
            result += 1

        while window or heap:
            if result - n in window:
                freq_pair = window.pop(result - n)
                heappush(heap, freq_pair)
            if heap:
                freq, ch = heappop(heap)
                if freq + 1 != 0:
                    window[result] = [freq + 1, ch]
            result += 1

        return result

    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Approach 2. Math + Counter, TC - O(N), SC - O(26) ~ O(1)
        counter = Counter(tasks)
        max_freq = max(counter.values())
        max_freq_count = Counter(counter.values())[max_freq]
        return max(len(tasks), (n + 1) * (max_freq - 1) + max_freq_count)


if __name__ == '__main__':
    solution = Solution()
    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 2
    result = solution.leastInterval(tasks, n)
    print(result)
    result = solution.leastInterval2(tasks, n)
    print(result)
