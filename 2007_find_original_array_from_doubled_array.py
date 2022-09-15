from collections import Counter
from typing import List


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        freq = Counter(changed)
        res, used = [], set()

        for num in freq.keys():
            if num in used:
                continue
            while num != 0 and num * 2 in freq:
                num *= 2
            while num in freq:
                if num == 0 or num % 2 == 1:
                    if num == 0 and freq[num] % 2 == 0:
                        res += [num] * (freq[num] // 2)
                    used.add(num)
                    break
                elif 0 < freq[num] <= freq.get(num // 2, 0):
                    res += [num // 2] * freq[num]
                    freq[num // 2] -= freq[num]
                used.add(num)
                num //= 2

        return res if len(res) == len(changed) / 2 else []


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 3, 4, 2, 6, 8]
    result = solution.findOriginalArray(nums)
    print(result)
