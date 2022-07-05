from collections import defaultdict
from typing import List


class Solution:
    def numOfMinutes(self, n: int, headID: int, managers: List[int], informTime: List[int]) -> int:
        tree = defaultdict(list)
        self.max_time = 0

        for empl, mang in enumerate(managers):
            tree[mang].append(empl)

        def dfs(tree, informTime, empl, time=0):
            if not tree[empl]:
                self.max_time = max(self.max_time, time)

            for next_empl in tree[empl]:
                dfs(tree, informTime, next_empl, time + informTime[empl])

        dfs(tree, informTime, headID)
        return self.max_time


if __name__ == '__main__':
    solution = Solution()
    n = 1
    headID = 0
    manager = [-1]
    informTime = [0]
    result = solution.numOfMinutes(n, headID, manager, informTime)
    print(result)
