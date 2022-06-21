from collections import defaultdict
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]):
        free_courses = []
        graph = defaultdict(list)
        inc_degrees = [0] * numCourses
        top_sort = []

        for p in prerequisites:
            graph[p[1]].append(p[0])
            inc_degrees[p[0]] += 1

        for node, req in enumerate(inc_degrees):
            if req == 0:
                free_courses.append(node)

        while free_courses:
            node = free_courses.pop()
            top_sort.append(node)

            for node_to in graph[node]:
                inc_degrees[node_to] -= 1
                if inc_degrees[node_to] == 0:
                    free_courses.append(node_to)

        if len(top_sort) == numCourses:
            return top_sort
        else:
            return []


if __name__ == '__main__':
    solution = Solution()
    numCourses = 4
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
    result = solution.findOrder(numCourses, prerequisites)
    print(result)
