from typing import List


class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                continue

            slow = fast = (nums[i] + i) % n
            fast = (nums[fast] + fast) % n

            while slow != fast:
                slow = (nums[slow] + slow) % n
                fast = (nums[fast] + fast) % n
                fast = (nums[fast] + fast) % n

            next_slow = (nums[slow] + slow) % n
            if slow != next_slow:
                while next_slow != fast:
                    if not ((nums[slow] > 0) == (nums[next_slow] > 0)):
                        break
                    slow = next_slow
                    next_slow = (nums[next_slow] + next_slow) % n
                else:
                    return True

            next_ind = i
            while nums[next_ind] != 0:
                nums[next_ind], next_ind = 0, (nums[next_ind] + next_ind) % n
        return False


if __name__ == '__main__':
    solution = Solution()
    nums = [2, -1, 1, 2, 2]
    result = solution.circularArrayLoop(nums.copy())
    print(result)
