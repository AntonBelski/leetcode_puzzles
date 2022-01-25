class Solution:
    def construct2DArray(self, original, m, n):
        matrix = []
        if len(original) == n * m:
            for i in range(m):
                row = [original[n * i + j] for j in range(n)]
                matrix.append(row)
        return matrix


if __name__ == '__main__':
    solution = Solution()
    my_nums = [[1, 2], 1, 1]
    res = solution.construct2DArray(*my_nums)
    print(res)
