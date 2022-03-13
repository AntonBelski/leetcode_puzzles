from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        start = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[start] = nums[i]
                start += 1

        return start


if __name__ == '__main__':
    solution = Solution()
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    solution.removeElement(nums, val)
    print(nums)
