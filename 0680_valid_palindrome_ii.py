from typing import List


class Solution:
    def validPalindrome(self, s: str) -> bool:
        def remove_chars(s, left, right, remain=1):  # left = 0, right = 2, remain = 1
            while left <= right:
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                    continue
                elif s[left] != s[right] and remain > 0:
                    return any([remove_chars(s, left + 1, right, remain - 1),
                                remove_chars(s, left, right - 1, remain - 1)])
                else:
                    return False
            return True

        return remove_chars(s, 0, len(s) - 1)


if __name__ == '__main__':
    solution = Solution()
    s = "abca"
    result = solution.validPalindrome(s)
    print(result)
