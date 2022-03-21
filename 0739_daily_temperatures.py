from typing import List


class Solution:
    def dailyTemperatures2(self, temps: List[int]) -> List[int]:
        # My Solution, Time Complexity - O(n), Space Complexity - O(n)
        result = [0] * len(temps)
        stack = []

        for i, t in enumerate(temps):
            while stack and temps[stack[-1]] < t:
                result[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)

        return result

    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        # Smarter Solution, Time Complexity - O(n), Space Complexity - O(1)
        result = [0] * len(temps)

        for i in range(len(temps) - 2, -1, -1):
            days = 1
            while temps[i] >= temps[i + days] and result[i + days] != 0:
                days += result[i + days]
            if temps[i] < temps[i + days]:
                result[i] = days

        return result


if __name__ == '__main__':
    solution = Solution()
    temps = [73, 74, 75, 71, 69, 72, 76, 73]
    result = solution.dailyTemperatures2(temps)
    print(result)
    result = solution.dailyTemperatures(temps)
    print(result)
