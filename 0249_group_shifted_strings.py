from collections import defaultdict
from typing import List


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        blocks = defaultdict(list)

        for s in strings:
            curr_hash = []
            for i in range(1, len(s)):
                prev_ch, ch = s[i - 1], s[i]
                ch_hash = (ord(ch) - ord(prev_ch)) % 26
                curr_hash.append(chr(ch_hash))

            blocks[''.join(curr_hash)].append(s)

        return list(blocks.values())


if __name__ == '__main__':
    solution = Solution()
    strings = ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
    result = solution.groupStrings(strings)
    print(result)
