from typing import List
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict


class Solution:
    def smallestRange2(self, nums: List[List[int]]) -> List[int]:
        # My Solution, Time Complexity - O(N*log(M)), Space Complexity - O(M), best asymptotic, but code is not clear
        heap = []
        result = [-float('inf'), float('inf')]
        for i, lst in enumerate(nums):
            heap.append([lst[0], i, 0])
            result = [min(result[0], lst[0]), max(result[1], lst[0])]
        rows_dict = {}
        range_dict = defaultdict(int)
        sorted_range = deque()

        heapify(heap)
        while heap:
            val, nums_ind, row_ind = heappop(heap)

            if row_ind + 1 < len(nums[nums_ind]):
                new_val = nums[nums_ind][row_ind + 1]
                heappush(heap, [new_val, nums_ind, row_ind + 1])

            if nums_ind in rows_dict:
                range_dict[rows_dict[nums_ind]] -= 1
            rows_dict[nums_ind] = val
            range_dict[val] += 1

            if not sorted_range or sorted_range[-1] != val:
                sorted_range.append(val)

            while range_dict[sorted_range[0]] == 0:
                sorted_range.popleft()

            if len(rows_dict) == len(nums):
                if sorted_range[-1] - sorted_range[0] < result[1] - result[0]:
                    result = [sorted_range[0], sorted_range[-1]]

        return result

    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # Smarter Solution, Time Complexity - O(N*log(M)), Space Complexity - O(M)
        # code is very clean, but logic is harder
        heap = []
        high = -float('inf')
        for i in range(len(nums)):
            heappush(heap, [nums[i][0], i, 0])
            high = max(high, nums[i][0])
        result = [heap[0][0], high]

        while True:
            val, nums_i, i = heappop(heap)
            if i + 1 == len(nums[nums_i]):
                break
            new_val = nums[nums_i][i + 1]
            heappush(heap, [new_val, nums_i, i + 1])
            high = max(high, new_val)
            if high - heap[0][0] < result[1] - result[0]:
                result = [heap[0][0], high]

        return result


if __name__ == '__main__':
    solution = Solution()
    nums = [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]
    result = solution.smallestRange(nums=nums)
    print(result)
    result = solution.smallestRange2(nums=nums)
    print(result)
