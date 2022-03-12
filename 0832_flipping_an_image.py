from math import ceil
from typing import List


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in range(len(image)):
            n = len(image[row])
            half_n = ceil(n / 2)

            for i in range(half_n):
                image[row][i], image[row][n - i - 1] = image[row][n - i - 1], image[row][i]
                image[row][i] = image[row][i] ^ 1

                if i != n - i - 1:
                    image[row][n - i - 1] = image[row][n - i - 1] ^ 1

        return image


if __name__ == '__main__':
    solution = Solution()
    nums = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
    result = solution.flipAndInvertImage(nums)
    print(result)
