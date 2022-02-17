from typing import List


class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        prev_n = None
        for s in s.split():
            if s.isdigit():
                if prev_n is None:
                    prev_n = int(s)
                elif prev_n >= int(s):
                    return False
                else:
                    prev_n = int(s)

        return True


if __name__ == '__main__':
    solution = Solution()
    s = "1 box has 3 blue 4 red 6 green and 12 yellow marbles"
    res = solution.areNumbersAscending(s)
    print(res)
