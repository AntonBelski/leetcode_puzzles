from typing import List
from heapq import heapify, heappop, heappush
from collections import defaultdict


class Solution2:
    # My First Solution, TC - O((n - k)*k*log(k)), SC - O(k)
    def find_median(self, max_heap, min_heap):
        if len(max_heap) > len(min_heap):
            return -max_heap[0]
        else:
            return (-max_heap[0] + min_heap[0]) / 2

    def add_num_to_heaps(self, num, max_heap, min_heap):
        heappush(max_heap, -num)
        heappush(min_heap, -heappop(max_heap))
        if len(min_heap) > len(max_heap):
            heappush(max_heap, -heappop(min_heap))

    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        max_heap = []
        min_heap = []
        result = []

        for i in range(k):
            self.add_num_to_heaps(nums[i], max_heap, min_heap)

        result.append(self.find_median(max_heap, min_heap))

        for i in range(k, len(nums)):
            prev_num = nums[i - k]
            if -prev_num in max_heap:
                max_heap.remove(-prev_num)
                heapify(max_heap)
                if len(max_heap) < len(min_heap):
                    heappush(max_heap, -heappop(min_heap))
            else:
                min_heap.remove(prev_num)
                heapify(min_heap)
                if len(max_heap) == len(min_heap) + 2:
                    heappush(min_heap, -heappop(max_heap))

            self.add_num_to_heaps(nums[i], max_heap, min_heap)
            result.append(self.find_median(max_heap, min_heap))

        return result


class Solution:
    # My Second (Improved) Solution, TC - O((n - k)*log(k)), SC - O(k)
    def find_median(self, max_heap, min_heap, heap_size):
        if heap_size % 2 == 1:
            return -max_heap[0]
        else:
            return (-max_heap[0] + min_heap[0]) / 2

    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        max_heap = []
        min_heap = []
        heap_dict = defaultdict(int)
        result = []

        for i in range(k):
            heappush(max_heap, -nums[i])
            heappush(min_heap, -heappop(max_heap))
            if len(min_heap) > len(max_heap):
                heappush(max_heap, -heappop(min_heap))

        median = self.find_median(max_heap, min_heap, k)
        result.append(median)

        for i in range(k, len(nums)):
            prev_num = nums[i - k]
            heap_dict[prev_num] += 1

            balance = -1 if prev_num <= median else 1

            if nums[i] <= median:
                balance += 1
                heappush(max_heap, -nums[i])
            else:
                balance -= 1
                heappush(min_heap, nums[i])

            if balance < 0:
                heappush(max_heap, -heappop(min_heap))
            elif balance > 0:
                heappush(min_heap, -heappop(max_heap))

            while max_heap and heap_dict[-max_heap[0]] > 0:
                heap_dict[-max_heap[0]] -= 1
                heappop(max_heap)

            while min_heap and heap_dict[min_heap[0]] > 0:
                heap_dict[min_heap[0]] -= 1
                heappop(min_heap)

            median = self.find_median(max_heap, min_heap, k)
            result.append(median)

        return result


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    result = solution.medianSlidingWindow(nums, k)
    print(result)
    solution = Solution2()
    result = solution.medianSlidingWindow(nums, k)
    print(result)
