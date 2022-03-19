from typing import List


class MyQueue:
    def __init__(self):
        self.stack_push = []
        self.stack_pop = []
        self.front_push = None

    def push(self, x: int) -> None:
        if not self.stack_push:
            self.front_push = x
        self.stack_push.append(x)

    def pop(self) -> int:
        if not self.stack_pop:
            while self.stack_push:
                self.stack_pop.append(self.stack_push.pop())
        if self.stack_pop:
            return self.stack_pop.pop()

    def peek(self) -> int:
        if self.stack_pop:
            return self.stack_pop[-1]
        elif self.stack_push:
            return self.front_push

    def empty(self) -> bool:
        return not self.stack_pop and not self.stack_push


if __name__ == '__main__':
    my_queue = MyQueue()
    print(my_queue.push(1))
    print(my_queue.push(2))
    print(my_queue.peek())
    print(my_queue.pop())
    print(my_queue.empty())
