from collections import deque
from typing import List


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        deq = deque()
        deq.append(start)
        visited = set()

        while deq:
            ind = deq.popleft()
            if not 0 <= ind < len(arr) or ind in visited:
                continue
            if arr[ind] == 0:
                return True

            visited.add(ind)
            deq.append(ind - arr[ind])
            deq.append(ind + arr[ind])

        return False


if __name__ == '__main__':
    solution = Solution()
    arr = [4, 2, 3, 0, 3, 1, 2]
    start = 5
    result = solution.canReach(arr, start)
    print(result)
