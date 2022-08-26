from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        def modify_elems(nums, is_modified=False, start=1):
            while start < len(nums) and nums[start - 1] <= nums[start]:
                start += 1

            is_valid = []
            if start == len(nums):
                return True
            elif not is_modified:
                for new_val in [nums[start - 1], nums[start]]:
                    prev, curr = nums[start - 1], nums[start]
                    nums[start - 1], nums[start] = new_val, new_val
                    is_valid.append(modify_elems(nums, is_modified=True))
                    nums[start - 1], nums[start] = prev, curr
            return any(is_valid)

        return modify_elems(nums)


if __name__ == '__main__':
    solution = Solution()
    nums = [4, 2, 3]
    result = solution.checkPossibility(nums)
    print(result)
