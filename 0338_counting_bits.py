class Solution:
    def countBits(self, n):
        result = [0, 1]
        for i in range(2, n + 1):
            result.append(result[i // 2] + i % 2)
        return result[:n + 1]


if __name__ == '__main__':
    solution = Solution()
    my_nums = 20
    res = solution.countBits(my_nums)
    print(res)
