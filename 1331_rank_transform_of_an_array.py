from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_add = sorted(arr)
        rank_dict = dict()

        rank = 1
        for elem in sorted_add:
            if elem not in rank_dict:
                rank_dict[elem] = rank
                rank += 1

        result = []
        for elem in arr:
            result.append(rank_dict[elem])

        return result


if __name__ == '__main__':
    solution = Solution()
    arr = [40, 10, 20, 30]
    result = solution.arrayRankTransform(arr)
    print(result)
