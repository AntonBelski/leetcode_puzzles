from typing import List


class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(str(num))
        stack = []
        swap_result = None

        for ind, digit in enumerate(num):
            while stack and num[stack[-1]] < digit:
                swap_result = [stack.pop(), ind]

            if not swap_result:
                if not stack or num[stack[-1]] > digit:
                    stack.append(ind)

            elif num[swap_result[1]] <= digit:
                swap_result[1] = ind

        if swap_result:
            first, second = swap_result
            num[first], num[second] = num[second], num[first]

        return int(''.join(num))


if __name__ == '__main__':
    solution = Solution()
    num = 2736
    result = solution.maximumSwap(num)
    print(result)
