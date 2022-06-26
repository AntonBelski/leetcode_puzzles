from typing import List


class Solution:
    def maxScore(self, points: List[int], k: int) -> int:
        curr_sum = 0

        for i in range(k):
            curr_sum += points[i]

        max_sum = curr_sum

        for i in range(-1, -k - 1, -1):
            curr_sum += points[i]
            curr_sum -= points[k + i]
            max_sum = max(max_sum, curr_sum)

        return max_sum


if __name__ == '__main__':
    solution = Solution()
    cardPoints = [1, 2, 3, 4, 5, 6, 1]
    k = 3
    result = solution.maxScore(cardPoints, k)
    print(result)
