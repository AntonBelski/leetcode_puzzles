class Solution:
    def isPalindrome(self, s: str) -> bool:
        # TC = O(N), SC = O(N)
        r = []

        for ch in s:
            if ch.isalnum():
                r.append(ch.lower())

        return r == r[::-1]

    def isPalindrome2(self, s: str) -> bool:
        # TC = O(N), SC = O(1)
        len_s = len(s)
        left, right = 0, len_s - 1

        while left < right:
            while left < len_s and not s[left].isalnum():
                left += 1
            while right > 0 and not s[right].isalnum():
                right -= 1

            if left < len_s and right >= 0 and left < right:
                if s[left].lower() != s[right].lower():
                    return False
                left += 1
                right -= 1

        return True


if __name__ == '__main__':
    solution = Solution()
    s = "A man, a plan, a canal: Panama"
    res = solution.isPalindrome(s)
    print(res)
    res = solution.isPalindrome2(s)
    print(res)
