class Solution:
    def maxSubArray(self, nums) -> int:
        curr_sum = nums[0]
        best_sum = curr_sum
        for elem in nums[1:]:
            curr_sum = max(elem, curr_sum + elem)
            best_sum = max(best_sum, curr_sum)
        return best_sum


if __name__ == '__main__':
    solution = Solution()
    result = solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    print(result)
