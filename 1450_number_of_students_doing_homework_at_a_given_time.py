from typing import List


class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        result = 0

        for i in range(len(startTime)):
            if startTime[i] <= queryTime <= endTime[i]:
                result += 1

        return result


if __name__ == '__main__':
    solution = Solution()
    startTime = [1, 2, 3]
    endTime = [3, 2, 7]
    queryTime = 4
    res = solution.busyStudent(startTime, endTime, queryTime)
    print(res)
