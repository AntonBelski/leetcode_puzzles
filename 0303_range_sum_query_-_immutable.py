from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        self.pref_sum = [0]
        for num in nums:
            self.pref_sum.append(self.pref_sum[-1] + num)

    def sumRange(self, left: int, right: int) -> int:
        return self.pref_sum[right + 1] - self.pref_sum[left]


if __name__ == '__main__':
    numArray = NumArray([-2, 0, 3, -5, 2, -1])
    print(numArray.sumRange(0, 2))
    print(numArray.sumRange(2, 5))
    print(numArray.sumRange(0, 5))
