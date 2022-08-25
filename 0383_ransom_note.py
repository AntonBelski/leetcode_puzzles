from collections import Counter
from typing import List


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r_counter = Counter(ransomNote)
        m_counter = Counter(magazine)

        for char, count in r_counter.items():
            if m_counter[char] < count:
                return False

        return True


if __name__ == '__main__':
    solution = Solution()
    ransomNote = "a"
    magazine = "b"
    result = solution.canConstruct(ransomNote, magazine)
    print(result)
