class Solution:
    def longestOnes(self, arr, k):
        ones_counter = 0
        start_ind = 0
        max_counter = 0

        for i in range(len(arr)):
            if arr[i] == 1:
                ones_counter += 1

            if i + 1 - start_ind > ones_counter + k:
                if arr[start_ind] == 1:
                    ones_counter -= 1
                start_ind += 1

            max_counter = max(max_counter, i + 1 - start_ind)

        return max_counter


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    k = 2
    res = solution.longestOnes(nums, k)
    print(res)
