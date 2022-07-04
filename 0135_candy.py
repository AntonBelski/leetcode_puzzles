from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        # Time Complexity - O(n), Space Complexity - O(n). First readable solution, but is not short code.
        down = 1
        up = 1
        last_up = 1
        result = 1

        for i in range(1, len(ratings)):
            if ratings[i - 1] > ratings[i]:
                if up > 1:
                    down -= 1
                down += 1
                if last_up > 1 and last_up == down:
                    down += 1
                up = 1
                result += down
            elif ratings[i - 1] < ratings[i]:
                up += 1
                down = 1
                last_up = up
                result += up
            else:
                up = 1
                down = 1
                last_up = up
                result += 1

        return result

    def candy2(self, ratings: List[int]) -> int:
        # Time Complexity - O(n), Space Complexity - O(n). Shorter version of the previous solution.
        down = up = last_up = 1
        result = 1

        for i in range(1, len(ratings)):
            if ratings[i - 1] > ratings[i]:
                down += 1
                if up > 1:
                    down -= 1
                    up = 1
                elif last_up > 1 and last_up == down:
                    down += 1
            elif ratings[i - 1] < ratings[i]:
                up += 1
                down = 1
                last_up = up
            else:
                down = up = last_up = 1

            result += max(down, up)

        return result


if __name__ == '__main__':
    solution = Solution()
    ratings = [1, 6, 10, 8, 7, 3, 2]
    result = solution.candy(ratings)
    print(result)
    result = solution.candy2(ratings)
    print(result)
