class Solution:
    def containsDuplicate(self, nums) -> bool:
        nums_freq = {}
        for elem in nums:
            if nums_freq.get(elem):
                nums_freq[elem] += 1
            else:
                nums_freq[elem] = 1

        for freq in nums_freq.values():
            if freq >= 2:
                return True

        return False


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 2, 3, 1]
    result = solution.containsDuplicate(nums)
    print(result)
