from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        results = []
        stack = []
        closest_dict = {}

        for n in nums2:
            while stack and stack[-1] < n:
                elem = stack.pop()
                closest_dict[elem] = n

            stack.append(n)

        while stack:
            elem = stack.pop()
            closest_dict[elem] = -1

        for n in nums1:
            closest_greater = closest_dict[n]
            results.append(closest_greater)

        return results


if __name__ == '__main__':
    solution = Solution()
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]
    result = solution.nextGreaterElement(nums1, nums2)
    print(result)
