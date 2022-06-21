from collections import defaultdict
from typing import List
from queue import Queue


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        free_courses = Queue()
        graph = defaultdict(list)
        inc_degrees = [0] * numCourses
        top_sort = []

        for p in prerequisites:
            graph[p[1]].append(p[0])
            inc_degrees[p[0]] += 1

        for node, req in enumerate(inc_degrees):
            if req == 0:
                free_courses.put(node)

        while not free_courses.empty():
            node = free_courses.get()
            top_sort.append(node)

            for node_to in graph[node]:
                inc_degrees[node_to] -= 1
                if inc_degrees[node_to] == 0:
                    free_courses.put(node_to)

        if len(top_sort) == numCourses:
            return True
        else:
            return False


if __name__ == '__main__':
    solution = Solution()
    numCourses = 2
    prerequisites = [[1, 0], [0, 1]]
    result = solution.canFinish(numCourses, prerequisites)
    print(result)
