from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(graph, paths, path, curr_node=0):
            if curr_node == len(graph) - 1:
                paths.append(path[:])

            for next_node in graph[curr_node]:
                path.append(next_node)
                dfs(graph, paths, path, next_node)
                path.pop()

        paths = []
        dfs(graph, paths, path=[0])
        return paths


if __name__ == '__main__':
    solution = Solution()
    graph = [[1, 2], [3], [3], []]
    result = solution.allPathsSourceTarget(graph)
    print(result)
