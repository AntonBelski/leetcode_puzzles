class File:
    def __init__(self, string):
        self.file = list(reversed(string))

    def read4(self, buf):
        for i in range(4):
            if not self.file:
                return i
            else:
                buf[i] = self.file.pop()
        return 4


class Solution:
    def read(self, buf, file, n):
        buf4 = [''] * 4
        start = 0
        while start < n and file.read4(buf4):
            for ch in buf4:
                if not ch or start == n:
                    break
                buf[start] = ch
                start += 1
            buf4 = [''] * 4

        return start


if __name__ == '__main__':
    solution = Solution()
    file = File('abc')
    buf = [' '] * 1000
    n = 4
    result = solution.read(buf, file, n)
    print(result)
