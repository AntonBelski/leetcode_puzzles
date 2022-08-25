from collections import deque, defaultdict
from typing import List


class Solution:
    def shortestAlternatingPaths(self, n, red_edges, blue_edges):
        graph = defaultdict(set)
        min_paths = [float('inf')] * n
        RED, BLUE = 0, 1

        for start, end in red_edges:
            graph[(start, RED)].add(end)

        for start, end in blue_edges:
            graph[(start, BLUE)].add(end)

        for start_color in [RED, BLUE]:
            visited_nodes = set()
            deq = deque()
            deq.append([0, 0, start_color])

            while deq:
                node, dist, color = deq.popleft()
                if (node, color) in visited_nodes:
                    continue
                min_paths[node] = min(min_paths[node], dist)
                visited_nodes.add((node, color))

                for node_to in graph[(node, color)]:
                    deq.append([node_to, dist + 1, color ^ 1])

        return [p if p != float('inf') else -1 for p in min_paths]


if __name__ == '__main__':
    solution = Solution()
    n = 3
    redEdges = [[0, 1], [1, 2]]
    blueEdges = []
    result = solution.shortestAlternatingPaths(n, redEdges, blueEdges)
    print(result)
