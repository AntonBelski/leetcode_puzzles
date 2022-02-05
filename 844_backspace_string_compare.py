class Solution:
    def convert_string(self, s):
        s_list = []
        s_b = 0

        for i in range(len(s)):
            elem = s[len(s) - i - 1]
            if elem != '#' and s_b == 0:
                s_list.append(elem)
            elif elem != '#' and s_b > 0:
                s_b -= 1
            else:
                s_b += 1

        return s_list

    def backspaceCompare(self, s: str, t: str) -> bool:
        s_conv = self.convert_string(s)
        t_conv = self.convert_string(t)

        return s_conv[::-1] == t_conv[::-1]


if __name__ == '__main__':
    solution = Solution()
    s = "ab#c"
    t = "ad#c"
    res = solution.backspaceCompare(s, t)
    print(res)
