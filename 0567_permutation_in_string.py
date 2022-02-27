from collections import Counter


class Solution:
    # solution for O(s*p), where p <= 26
    def check_inclusion(self, pattern: str, str1: str) -> bool:
        k = len(pattern)
        pattern_dict = Counter(pattern)
        window_dict = Counter(str1[:k])

        if pattern_dict == window_dict:
            return True

        for window_end in range(k, len(str1)):
            first_window_elem = str1[window_end - k]
            if window_dict[first_window_elem] == 1:
                del window_dict[first_window_elem]
            else:
                window_dict[first_window_elem] -= 1

            new_elem = str1[window_end]
            if new_elem in window_dict:
                window_dict[new_elem] += 1
            else:
                window_dict[new_elem] = 1

            if pattern_dict == window_dict:
                return True

        return False

    # solution for O(s + p)
    def check_inclusion1(self, pattern: str, str1: str) -> bool:
        pattern_dict = {}
        str1_dict = {}
        k = len(pattern)
        matches = 0

        if k > len(str1):
            return False

        for i in range(ord('a'), ord('z') + 1):
            pattern_dict[chr(i)] = 0
            str1_dict[chr(i)] = 0

        for i in range(k):
            pattern_dict[pattern[i]] += 1
            str1_dict[str1[i]] += 1

        for i in range(ord('a'), ord('z') + 1):
            if pattern_dict[chr(i)] == str1_dict[chr(i)]:
                matches += 1

        if matches == 26:
            return True

        for window_end in range(k, len(str1)):
            window_end_elem = str1[window_end]
            str1_dict[window_end_elem] += 1
            if str1_dict[window_end_elem] == pattern_dict[window_end_elem]:
                matches += 1
            elif str1_dict[window_end_elem] - 1 == pattern_dict[window_end_elem]:
                matches -= 1

            window_start_elem = str1[window_end - k]
            str1_dict[window_start_elem] -= 1
            if str1_dict[window_start_elem] == pattern_dict[window_start_elem]:
                matches += 1
            elif str1_dict[window_start_elem] + 1 == pattern_dict[window_start_elem]:
                matches -= 1

            if matches == 26:
                return True

        return False


if __name__ == '__main__':
    solution = Solution()
    pattern = "mart"
    str1 = "karma"
    res1 = solution.check_inclusion(pattern=pattern, str1=str1)
    res2 = solution.check_inclusion1(pattern=pattern, str1=str1)
    print(res1)
    print(res2)
