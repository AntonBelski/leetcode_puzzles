from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        pairs = sorted(intervals)
        result = [pairs[0]]

        for pair in pairs[1:]:
            if result[-1][1] >= pair[0]:
                result[-1][1] = max(result[-1][1], pair[1])
            else:
                result.append(pair)

        return result


if __name__ == '__main__':
    solution = Solution()
    nums = [[1, 3], [2, 6], [8, 10], [15, 18]]
    res = solution.merge(nums)
    print(res)
