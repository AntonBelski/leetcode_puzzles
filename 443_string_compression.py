from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        ch = chars[0]
        ch_count = 1
        ind = 0

        for i in range(1, len(chars)):
            elem = chars[i]
            if elem == ch:
                ch_count += 1
            else:
                if ch_count == 1:
                    chars[ind] = ch
                    ind += 1
                else:
                    comp = ch + str(ch_count)
                    chars[ind:ind + len(comp)] = comp
                    ind += len(comp)

                ch = chars[i]
                ch_count = 1

        if ch_count == 1:
            chars[ind] = ch
            ind += 1
        else:
            comp = ch + str(ch_count)
            chars[ind:ind + len(comp)] = comp
            ind += len(comp)

        return ind


if __name__ == '__main__':
    solution = Solution()
    chars = ["a", "a", "b", "b", "c", "c", "c"]
    res = solution.compress(chars)
    print(res)
