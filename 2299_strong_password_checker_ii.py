from typing import List


class Solution:
    def strongPasswordCheckerII(self, st) -> bool:
        r = [False] * 5 + [True]
        for i, c in enumerate(st):
            r[0] = any([r[0], +(c.islower())])
            r[1] = any([r[1], +(c.isupper())])
            r[2] = any([r[2], +(c.isdigit())])
            r[3] = any([r[3], +(c in "!@#$%^&*()-+")])
            r[4] = any([r[4], +(i > 6)])
            if i > 0 and st[i - 1] == st[i]:
                r[5] = False

        return all(r)


if __name__ == '__main__':
    solution = Solution()
    password = "IloveLe3tcode!"
    result = solution.strongPasswordCheckerII(password)
    print(result)
