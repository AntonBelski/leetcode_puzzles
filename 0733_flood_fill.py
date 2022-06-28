from collections import deque
from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, new_color: int) -> List[List[int]]:
        old_color = image[sr][sc]
        deq = deque()
        deq.append([sr, sc])

        while deq:
            r, c = deq.popleft()
            if image[r][c] != new_color:
                image[r][c] = new_color
            else:
                continue

            if r > 0 and image[r - 1][c] == old_color:
                deq.append([r - 1, c])
            if r < len(image) - 1 and image[r + 1][c] == old_color:
                deq.append([r + 1, c])
            if c > 0 and image[r][c - 1] == old_color:
                deq.append([r, c - 1])
            if c < len(image[0]) - 1 and image[r][c + 1] == old_color:
                deq.append([r, c + 1])

        return image


if __name__ == '__main__':
    solution = Solution()
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    sr = 1
    sc = 1
    color = 2
    result = solution.floodFill(image, sr, sc, color)
    print(result)
