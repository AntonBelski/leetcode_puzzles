from typing import List


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        s_counter = {}
        counter = 0
        longest_str = 0
        start_ind = 0
        for i in range(len(s)):
            counter += 1
            if s_counter.get(s[i]):
                s_counter[s[i]] += 1
            else:
                s_counter[s[i]] = 1

            while len(s_counter) > k:
                s_counter[s[start_ind]] -= 1
                if not s_counter.get(s[start_ind]):
                    s_counter.pop(s[start_ind])
                start_ind += 1
                counter -= 1

            longest_str = max(longest_str, counter)
        return longest_str


if __name__ == '__main__':
    solution = Solution()
    s = "eceba"
    k = 2
    result = solution.lengthOfLongestSubstringKDistinct(s, k)
    print(result)
