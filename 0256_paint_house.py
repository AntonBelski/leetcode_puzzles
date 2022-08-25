from collections import defaultdict
from typing import List


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        default = defaultdict(lambda: float('inf'))
        curr_layer, next_layer = {}, default.copy()

        for i in range(3):
            curr_layer[i] = costs[0][i]

        for i in range(1, len(costs)):
            for color, cost in curr_layer.items():
                for to_color in [1, -1]:
                    new_color = (color + to_color) % 3
                    next_layer[new_color] = min(next_layer[new_color],
                                                cost + costs[i][new_color])
            curr_layer, next_layer = next_layer, default.copy()

        return min(curr_layer.values())


if __name__ == '__main__':
    solution = Solution()
    costs = [[17, 2, 17], [16, 16, 5], [14, 3, 19]]
    result = solution.minCost(costs)
    print(result)
