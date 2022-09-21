from typing import List


class Solution:
    def generate(self, size: int) -> List[List[int]]:
        res = [[1]]
        for layer in range(1, size):
            res.append([1])
            for i in range(1, layer):
                res[-1].append(res[-2][i] + res[-2][i - 1])
            res[-1].append(1)
        return res


if __name__ == '__main__':
    solution = Solution()
    n = 9
    result = solution.generate(n)
    print(result)
