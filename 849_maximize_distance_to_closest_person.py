from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        empty_seats = 0
        max_empty_seats = 0

        start = 0
        end = len(seats) - 1

        while seats[start] == 0 or seats[end] == 0:
            if seats[start] == 0:
                start += 1
            if seats[end] == 0:
                end -= 1

        for elem in seats[start:end + 1]:
            if elem == 0:
                empty_seats += 1
            else:
                empty_seats = 0

            max_empty_seats = max(max_empty_seats, empty_seats)

        return max((max_empty_seats + 1) // 2, start, len(seats) - 1 - end)


if __name__ == '__main__':
    solution = Solution()
    seats = [1, 0, 0, 0, 1, 0, 1]
    res = solution.maxDistToClosest(seats)
    print(res)
