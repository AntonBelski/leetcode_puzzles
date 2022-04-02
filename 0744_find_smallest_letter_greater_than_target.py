from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        lo = 0
        hi = len(letters) - 1

        while lo != hi:
            mid = (lo + hi) // 2
            if target >= letters[mid]:
                lo = mid + 1
            else:
                hi = mid

        if letters[lo] > target:
            return letters[lo]
        else:
            return letters[0]


if __name__ == '__main__':
    solution = Solution()
    letters = ["c", "f", "j"]
    target = "a"
    result = solution.nextGreatestLetter(letters, target)
    print(result)
