from typing import List


class MinStack:
    def __init__(self):
        self.stack = []
        self.min_val = 0

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append([val, val])
        else:
            new_min_val = min(val, self.stack[-1][-1])
            self.stack.append([val, new_min_val])

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


if __name__ == '__main__':
    min_stack = MinStack()
    print(min_stack.push(-2))
    print(min_stack.push(0))
    print(min_stack.push(-3))
    print(min_stack.getMin())
    print(min_stack.pop())
    print(min_stack.top())
    print(min_stack.getMin())
