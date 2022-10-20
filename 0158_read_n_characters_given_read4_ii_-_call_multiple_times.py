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
    # since we're reading FIRST N characters from buf, and we return
    # we don't need to delete anything from buf, we can simply REPLACE first values with starting index 0 (to n)
    def __init__(self):
        self.buff = []

    def read(self, buf, file, n):
        pointer = 0

        while pointer < n:
            if not self.buff:
                self.buff = [''] * 4
                if file.read4(self.buff) == 0:
                    break
            else:
                buf[pointer] = self.buff.pop(0)
                pointer += 1

        return pointer


if __name__ == '__main__':
    solution = Solution()
    file = File('abc')
    buf = [' '] * 1000
    n = 4
    result = []

    for area in [1, 2, 1]:
        used_area = solution.read(buf, file, area)
        result.append(''.join(buf[:used_area]))

    print(result)
