class Solution:
    def isPalindrome(self, s: str) -> bool:
        r = []

        for ch in s:
            if ch.isalnum():
                r.append(ch.lower())

        return r == r[::-1]


if __name__ == '__main__':
    solution = Solution()
    s = "A man, a plan, a canal: Panama"
    res = solution.isPalindrome(s)
    print(res)
