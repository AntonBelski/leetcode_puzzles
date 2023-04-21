class Solution:
    def reverseWords(self, s: str) -> str:
        # TC = O(N), SC = O(N)
        return ' '.join(reversed(s.split()))

    def reverseWords2(self, s: str) -> str:
        # without split and reverse
        # TC = O(N), SC = O(N)
        result, word = [], []

        for i in range(len(s)):
            if s[i] != ' ':
                word.append(s[i])
            elif word:
                result.append(''.join(word))
                word = []

        if word:
            result.append(''.join(word))

        result.reverse()
        return ' '.join(result)


if __name__ == '__main__':
    solution = Solution()
    s = "the sky is blue"
    res = solution.reverseWords(s)
    print(res)
    res = solution.reverseWords2(s)
    print(res)
