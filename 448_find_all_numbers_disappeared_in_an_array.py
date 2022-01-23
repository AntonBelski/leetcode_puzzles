class Solution:
    def findDisappearedNumbers(self, nums):
        n = len(nums)
        for i in range(n):
            elem = abs(nums[i]) - 1
            if nums[elem] > 0:
                nums[elem] *= -1
        results = []
        for i in range(n):
            if nums[i] > 0:
                results.append(i + 1)
        return results


if __name__ == '__main__':
    solution = Solution()
    result = solution.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 8])
    print(result)
