from collections import Counter
from typing import List


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


if __name__ == '__main__':
    solution = Solution()
    s = "anagram"
    t = "nagaram"
    result = solution.isAnagram(s, t)
    print(result)
