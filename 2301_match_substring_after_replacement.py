from collections import defaultdict
from typing import List


class Solution:
    def matchReplacement(self, s: str, sub: str, mappings: List[List[str]]) -> bool:
        mappings_dict = defaultdict(set)
        for old, new in mappings:
            mappings_dict[old].add(new)

        for i, ch in enumerate(s):
            if i > len(s) - len(sub):
                break
            for y in range(len(sub)):
                if sub[y] == s[y + i]:
                    continue
                if s[y + i] in mappings_dict[sub[y]]:
                    continue
                break
            else:
                return True

        return False


if __name__ == '__main__':
    solution = Solution()
    s = "fool3e7bar"
    sub = "leet"
    mappings = [["e", "3"], ["t", "7"], ["t", "8"]]
    result = solution.matchReplacement(s, sub, mappings)
    print(result)
