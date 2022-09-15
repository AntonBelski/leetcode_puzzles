from typing import List


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        EQUAL, BIGGER, LESS = 0, 1, 2

        prev_comp = EQUAL
        curr_len = max_len = 1

        for i in range(1, len(arr)):
            if arr[i - 1] > arr[i]:
                if prev_comp != BIGGER:
                    curr_len += 1
                else:
                    curr_len = 2
                prev_comp = BIGGER
            elif arr[i - 1] < arr[i]:
                if prev_comp != LESS:
                    curr_len += 1
                else:
                    curr_len = 2
                prev_comp = LESS
            else:
                prev_comp = EQUAL
                curr_len = 1

            max_len = max(max_len, curr_len)

        return max_len


if __name__ == '__main__':
    solution = Solution()
    arr = [9, 4, 2, 10, 7, 8, 8, 1, 9]
    result = solution.maxTurbulenceSize(arr)
    print(result)
