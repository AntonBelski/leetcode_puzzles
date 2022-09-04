from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # My Solution, Time Complexity - O(m), Space Complexity - O(m), where m = length of the longest string
        pref = list(strs[0])
        pref.append('')

        for s in strs:
            for i, ch in enumerate(pref):
                if ch == '' or i >= len(s) or ch != s[i]:
                    pref[i] = ''
                    break

        size = pref.index('')
        return ''.join(pref[:size])

    def longestCommonPrefix2(self, strs: List[str]) -> str:
        # Optimized Solution, Time Complexity - O(m), Space Complexity - O(1), where m = length of the longest string
        pref = [0, len(strs[0])]

        for s_i in range(1, len(strs)):
            for i in range(pref[1]):
                if i >= len(strs[s_i]) or strs[s_i][i] != strs[s_i - 1][i]:
                    pref[1] = i
                    break

        return strs[0][pref[0]:pref[1]]


if __name__ == '__main__':
    solution = Solution()
    strs = ["flower", "flow", "flight"]
    result = solution.longestCommonPrefix(strs)
    print(result)
    result = solution.longestCommonPrefix2(strs)
    print(result)
