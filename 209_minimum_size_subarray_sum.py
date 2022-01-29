class Solution:
    def minSubArrayLen(self, target, nums):
        start_ind = 0
        curr_sum = 0
        result = float('inf')

        for i in range(len(nums)):
            elem = nums[i]
            curr_sum += elem
            while curr_sum >= target:
                result = min(result, i + 1 - start_ind)
                curr_sum -= nums[start_ind]
                start_ind += 1

        return result if result < float('inf') else 0


if __name__ == '__main__':
    solution = Solution()
    target = 7
    nums = [2, 3, 1, 2, 4, 3]
    res = solution.minSubArrayLen(target, nums)
    print(res)
