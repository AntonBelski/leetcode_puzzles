from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        start_ind = 1
        prev_elem = nums[0]

        for elem in nums[1:]:
            if prev_elem != elem:
                nums[start_ind] = elem
                start_ind += 1
            prev_elem = elem

        return start_ind


if __name__ == '__main__':
    solution = Solution()
    numbers = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    res = solution.removeDuplicates(numbers)
    print(res)
