from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        lo, hi = 0, len(letters)
        while lo != hi:
            mid = (lo + hi) // 2
            if target < letters[mid]:
                hi = mid
            else:
                lo = mid + 1

        return letters[lo % len(letters)]


if __name__ == '__main__':
    solution = Solution()
    letters = ["c", "f", "j"]
    target = "a"
    result = solution.nextGreatestLetter(letters, target)
    print(result)
