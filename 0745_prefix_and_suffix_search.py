from typing import List
from collections import defaultdict


class WordFilter:
    def __init__(self, w: List[str]):
        inf_defaultdict = lambda: defaultdict(inf_defaultdict)
        p_d = inf_defaultdict()
        s_d = inf_defaultdict()
        self.results = inf_defaultdict()

        for i, word in enumerate(w):
            sz = len(word) - 1
            if 0 not in p_d[sz]:
                p_d[sz][0] = set()
                s_d[sz][0] = set()
            p_d[sz][0].add(i)
            s_d[sz][0].add(i)

        def prefix_chars(w, d, max_depth, depth=0, is_reverse=False):
            if type(d) != defaultdict or depth > max_depth:
                return
            for i in d[0]:
                ch = w[i][depth if not is_reverse else max_depth - depth]
                if 0 not in d[ch]:
                    d[ch][0] = set()
                d[ch][0].add(i)
            for ch in d:
                prefix_chars(w, d[ch], max_depth, depth + 1, is_reverse)

        for i in range(10):
            prefix_chars(w, p_d[i], i)
            prefix_chars(w, s_d[i], i, is_reverse=True)

        self.p_d = p_d
        self.s_d = s_d

    def f(self, prefix: str, suffix: str) -> int:
        min_len = max(len(prefix), len(suffix))
        max_ind = -1
        start = 9
        if suffix in self.results[prefix]:
            return self.results[prefix][suffix]
        while start + 1 >= min_len:
            pref_inds = self.p_d[start]
            for ch in prefix:
                if ch in pref_inds:
                    pref_inds = pref_inds[ch]
                else:
                    pref_inds = {}
                    break
            suff_inds = self.s_d[start]
            for i in range(len(suffix) - 1, -1, -1):
                ch = suffix[i]
                if ch in suff_inds:
                    suff_inds = suff_inds[ch]
                else:
                    suff_inds = {}
                    break
            if 0 in pref_inds and 0 in suff_inds:
                matches = pref_inds[0].intersection(suff_inds[0])
                if matches:
                    max_ind = max(max_ind, max(matches))
            start -= 1
        self.results[prefix][suffix] = max_ind
        return max_ind


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)

if __name__ == '__main__':
    words = ["cabaabaaaa",  # 0
             "ccbcababac",  # 1
             "bacaabccba",  # 2
             "bcbbcbacaa",  # 3
             "abcaccbcaa",  # 4
             "accabaccaa",  # 5
             "cabcbbbcca",  # 6
             "ababccabcb",  # 7
             "caccbbcbab",  # 8
             "bccbacbcba"]  # 9
    tests = [["bccbacbcba", "a"], ["ab", "abcaccbcaa"], ["a", "aa"], ["cabaaba", "abaaaa"], ["cacc", "accbbcbab"],
             ["ccbcab", "bac"], ["bac", "cba"], ["ac", "accabaccaa"], ["bcbb", "aa"], ["ccbca", "cbcababac"]]
    word_filter = WordFilter(words)
    results = []
    for pref, suf in tests:
        results.append(str(word_filter.f(pref, suf)))

    print(' '.join(results))
