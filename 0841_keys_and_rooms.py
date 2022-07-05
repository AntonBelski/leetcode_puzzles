from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        blocks = [False] * len(rooms)
        blocks[0] = True
        stack = [0]

        while stack:
            ind = stack.pop()
            for room_to in rooms[ind]:
                if not blocks[room_to]:
                    blocks[room_to] = True
                    stack.append(room_to)

        return all(blocks)


if __name__ == '__main__':
    solution = Solution()
    rooms = [[1, 3], [3, 0, 1], [2], [0]]
    result = solution.canVisitAllRooms(rooms)
    print(result)
