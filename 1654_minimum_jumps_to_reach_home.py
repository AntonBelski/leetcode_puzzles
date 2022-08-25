from collections import deque
from typing import List


class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        visited = {place: -1 for place in forbidden}
        LEFT, RIGHT = 0, 1
        deq = deque()
        deq.append([0, 0, RIGHT])

        while deq:
            curr, path, direction = deq.popleft()
            if not 0 <= curr <= (x + b) * 10 or curr in visited:
                continue
            if curr == x:
                return path

            visited[curr] = path
            if direction == RIGHT:
                deq.append([curr - b, path + 1, LEFT])
            deq.append([curr + a, path + 1, RIGHT])

        return -1


if __name__ == '__main__':
    solution = Solution()
    forbidden = [14, 4, 18, 1, 15]
    a = 3
    b = 15
    x = 9
    result = solution.minimumJumps(forbidden, a, b, x)
    print(result)
