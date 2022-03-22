from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            while stack and a < 0 < stack[-1]:
                if stack[-1] < abs(a):
                    stack.pop()
                else:
                    if stack[-1] + a == 0:
                        stack.pop()
                    break
            else:
                stack.append(a)

        return stack


if __name__ == '__main__':
    solution = Solution()
    asteroids = [5, 10, -5]
    result = solution.asteroidCollision(asteroids)
    print(result)
