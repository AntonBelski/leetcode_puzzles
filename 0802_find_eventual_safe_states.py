from collections import defaultdict
from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        reverse_graph = defaultdict(set)
        blocks = [0] * len(graph)
        result = [-1] * len(graph)
        stack = []

        for ind, nodes_to in enumerate(graph):
            if not nodes_to:
                stack.append(ind)
            for node in nodes_to:
                reverse_graph[node].add(ind)
                blocks[ind] += 1

        while stack:
            node_from = stack.pop()
            result[node_from] = node_from

            for node_to in reverse_graph[node_from]:
                blocks[node_to] -= 1
                if blocks[node_to] == 0:
                    stack.append(node_to)

        return [node for node in result if node != -1]


if __name__ == '__main__':
    solution = Solution()
    graph = [[1, 2], [2, 3], [5], [0], [5], [], []]
    result = solution.eventualSafeNodes(graph)
    print(result)
