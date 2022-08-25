from typing import List


class Solution:
    def simplifyPath(self, path: str) -> str:
        res = []
        for part in path.split('/'):
            if part == '..':
                if res:
                    res.pop()
            elif part and part != '.':
                res.append(part)
        return '/' + '/'.join(res)


if __name__ == '__main__':
    solution = Solution()
    path = "/home/"
    result = solution.simplifyPath(path)
    print(result)
