from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        shortest_paths = [float('inf')] * n
        heap = []

        for u, v, w in times:
            graph[u - 1].append([v - 1, w])

        shortest_paths[k - 1] = 0
        heappush(heap, [0, k - 1])

        while heap:
            from_dist, from_node = heappop(heap)
            if from_dist > shortest_paths[from_node]:
                continue
            for to_node, to_dist in graph[from_node]:
                new_dist = from_dist + to_dist
                if new_dist < shortest_paths[to_node]:
                    shortest_paths[to_node] = new_dist
                    heappush(heap, [new_dist, to_node])

        if float('inf') in shortest_paths:
            return -1
        else:
            return max(shortest_paths)


if __name__ == '__main__':
    solution = Solution()
    times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    n = 4
    k = 2
    result = solution.networkDelayTime(times, n, k)
    print(result)
