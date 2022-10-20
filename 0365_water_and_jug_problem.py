from typing import List
from collections import deque


class Solution:
    def canMeasureWater(self, a: int, b: int, target: int) -> bool:
        used_pairs = set(tuple([0, 0]))
        queue = deque()
        queue.append([0, 0, 0])

        while queue:
            curr_a, curr_b, depth = queue.popleft()

            if curr_a + curr_b == target:
                return True

            pour_to_a = min(a, curr_a + curr_b)
            pour_from_b = curr_b - (pour_to_a - curr_a)

            pour_to_b = min(b, curr_a + curr_b)
            pour_from_a = curr_a - (pour_to_b - curr_b)

            choices = [[a, curr_b], [curr_a, b],
                       [0, curr_b], [curr_a, 0],
                       [pour_to_a, pour_from_b],
                       [pour_from_a, pour_to_b]]

            for choice in choices:
                if tuple(choice) not in used_pairs:
                    used_pairs.add(tuple(choice))
                    next_a, next_b = choice
                    queue.append([next_a, next_b, depth + 1])

        return False


if __name__ == '__main__':
    solution = Solution()
    a = 3
    b = 5
    target = 4
    result = solution.canMeasureWater(a, b, target)
    print(result)
