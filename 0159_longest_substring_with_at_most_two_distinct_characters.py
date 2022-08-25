from collections import defaultdict
from typing import List


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        window = defaultdict(int)
        max_len = 0
        start = 0

        for ind, ch in enumerate(s):
            window[ch] += 1
            while len(window) > 2:
                window[s[start]] -= 1
                if window[s[start]] == 0:
                    del window[s[start]]
                start += 1
            max_len = max(max_len, ind + 1 - start)

        return max_len


if __name__ == '__main__':
    solution = Solution()
    s = "eceba"
    result = solution.lengthOfLongestSubstringTwoDistinct(s)
    print(result)
