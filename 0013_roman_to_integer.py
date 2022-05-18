from typing import List


class Solution:
    def romanToInt2(self, s: str) -> int:
        # First Solution
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        prev = num = roman_dict[s[0]]
        for r in s[1:]:
            curr = roman_dict[r]
            if num == 0:
                num += curr
            elif prev < curr:
                result += curr - num
                num = 0
            elif prev >= curr:
                result += num
                num = curr
            prev = curr
        result += num
        return result

    def romanToInt(self, s: str) -> int:
        # Second Solution with cleaner code after checking leetcode discuss
        to_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = i = 0
        while i < len(s):
            if i + 1 != len(s) and to_int[s[i]] < to_int[s[i + 1]]:
                result += to_int[s[i + 1]] - to_int[s[i]]
                i += 2
            else:
                result += to_int[s[i]]
                i += 1
        return result


if __name__ == '__main__':
    solution = Solution()
    s = "MCMXCIV"
    result = solution.romanToInt(s)
    print(result)
    result = solution.romanToInt2(s)
    print(result)
