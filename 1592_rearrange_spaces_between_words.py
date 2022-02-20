from typing import List


class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = text.split()
        spaces_count = text.count(' ')
        results = [words[0]]

        if len(words) > 1:
            dist, end_spaces = divmod(spaces_count, (len(words) - 1))
            for i in range(1, len(words)):
                results.append(' ' * dist)
                results.append(words[i])
            results.append(' ' * end_spaces)
        else:
            results.append(' ' * spaces_count)

        return ''.join(results)


if __name__ == '__main__':
    solution = Solution()
    text = "  this   is  a sentence "
    res = solution.reorderSpaces(text)
    print(res)
