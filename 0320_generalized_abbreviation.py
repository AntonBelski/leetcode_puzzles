from typing import List


class Solution:
    # Time Complexity - O(2^n * n), Space Complexity - O(n).
    def generateAbbreviations(self, word: str) -> List[str]:
        result, current = [str(len(word))], []
        self.backtrack(word, result, current)
        return result

    def backtrack(self, word, result, current, start=0, prev=-1):
        for i in range(start, len(word)):
            left = i - prev - 1 if prev + 1 != i else ''
            right = len(word) - 1 - i if i != len(word) - 1 else ''
            current.append(str(left) + word[i])
            result.append(''.join(current) + str(right))
            self.backtrack(word, result, current, i + 1, i)
            current.pop()


if __name__ == '__main__':
    solution = Solution()
    word = "word"
    result = solution.generateAbbreviations(word)
    print(result)
