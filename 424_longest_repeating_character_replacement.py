class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        s_dict = {}
        start_ind = 0
        max_ch = 0

        for i in range(len(s)):
            ch = s[i]
            if s_dict.get(ch):
                s_dict[ch] += 1
            else:
                s_dict[ch] = 1

            max_ch = max(max_ch, s_dict[ch])

            if i + 1 - start_ind > max_ch + k:
                s_dict[s[start_ind]] -= 1
                start_ind += 1

        return min(len(s), k + max_ch)


if __name__ == '__main__':
    solution = Solution()
    s = "ABAB"
    k = 2
    res = solution.characterReplacement(s, k)
    print(res)
