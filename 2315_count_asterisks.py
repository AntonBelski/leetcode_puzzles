from typing import List


class Solution:
    def countAsterisks(self, s: str) -> int:
        result = 0
        counter = 0
        for ch in s:
            if ch == '*' and counter % 2 == 0:
                result += 1
            if ch == '|':
                counter += 1
        return result


if __name__ == '__main__':
    solution = Solution()
    s = "l|*e*et|c**o|*de|"
    result = solution.countAsterisks(s)
    print(result)
