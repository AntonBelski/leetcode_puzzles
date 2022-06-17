from collections import defaultdict
from typing import List


class Solution:
    def is_next_chain(self, w1, w2):
        add_ch = 0
        for i in range(len(w1)):
            if w1[i] != w2[i + add_ch]:
                if add_ch == 0 and w1[i] == w2[i + 1]:
                    add_ch = 1
                else:
                    return False
        return True

    def longestStrChain(self, words: List[str]) -> int:
        dict_w = defaultdict(list)
        max_chain = 1

        for word in words:
            dict_w[len(word)].append([word, 1])

        for i in sorted(dict_w.keys()):
            for w_from, chain1 in dict_w[i - 1]:
                for ind_to, pair in enumerate(dict_w[i]):
                    if self.is_next_chain(w_from, pair[0]):
                        dict_w[i][ind_to][1] = max(dict_w[i][ind_to][1], chain1 + 1)
                        max_chain = max(max_chain, chain1 + 1)

        return max_chain


if __name__ == '__main__':
    solution = Solution()
    words = ["a", "b", "ba", "bca", "bda", "bdca"]
    result = solution.longestStrChain(words)
    print(result)
