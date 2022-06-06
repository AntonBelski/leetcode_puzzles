from typing import List


class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        _x, _y = abs(x), abs(y)
        _x, _y = min(_x, _y), max(_x, _y)
        y_base = (_y + 3) // 2
        mod_y_base = y_base if _y % 2 == 0 else y_base + 1
        if _x + 1 <= mod_y_base:
            circle = y_base
        else:
            circle = y_base + 1 + (_x - mod_y_base) // 3

        if circle == 2 and [_x, _y] != [1, 2] or [_x, _y] == [2, 2]:
            return _x + _y if _x + _y != 1 else 3

        is_even_circle_decrease = circle % 2 == 0 and _x % 2 != _y % 2
        is_odd_circle_decrease = circle % 2 == 1 and _x % 2 == _y % 2

        if is_even_circle_decrease or is_odd_circle_decrease:
            circle -= 1

        return circle


if __name__ == '__main__':
    solution = Solution()
    x = 5
    y = 5
    result = solution.minKnightMoves(x, y)
    print(result)

