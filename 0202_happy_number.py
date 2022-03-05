class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = n

        while fast != 1:
            slow = self.get_next(slow)
            fast = self.get_next(self.get_next(fast))

            if slow == fast and fast != 1:
                return False

        return True

    def get_next(self, n):
        return sum([int(d) ** 2 for d in str(n)])


if __name__ == '__main__':
    solution = Solution()
    n = 19
    res = solution.isHappy(n)
    print(res)
