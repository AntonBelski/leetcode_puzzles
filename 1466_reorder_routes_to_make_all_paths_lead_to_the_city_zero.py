from collections import defaultdict
from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        undir_graph = defaultdict(set)
        graph = defaultdict(set)

        for start, end in connections:
            graph[start].add(end)
            undir_graph[start].add(end)
            undir_graph[end].add(start)

        def dfs(undir_graph, graph, node=0, prev=-1):
            reverses = 0
            if prev != -1 and prev not in graph[node]:
                reverses += 1

            for node_to in undir_graph[node]:
                if node_to != prev:
                    reverses += dfs(undir_graph, graph, node_to, node)

            return reverses

        return dfs(undir_graph, graph)


if __name__ == '__main__':
    solution = Solution()
    n = 6
    connections = [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]
    result = solution.minReorder(n, connections)
    print(result)
