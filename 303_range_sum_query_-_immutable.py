class NumArray:
    def __init__(self, nums):
        self.sum_nums = nums[:1]
        for elem in nums[1:]:
            self.sum_nums.append(self.sum_nums[-1] + elem)

    def sumRange(self, left: int, right: int) -> int:
        left_sum = self.sum_nums[left - 1] if left > 0 else 0
        return self.sum_nums[right] - left_sum


if __name__ == '__main__':
    numArray = NumArray([-2, 0, 3, -5, 2, -1])
    print(numArray.sumRange(0, 2))
    print(numArray.sumRange(2, 5))
    print(numArray.sumRange(0, 5))
