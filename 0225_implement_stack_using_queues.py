from queue import Queue


class MyStack:
    def __init__(self):
        self.queue = Queue()
        self.front = None
        self.size = 0

    def push(self, x: int) -> None:
        self.queue.put(x)
        self.size += 1
        self.front = x

    def pop(self) -> int:
        for _ in range(self.size - 1):
            elem = self.queue.get()
            self.queue.put(elem)
            self.front = elem
        if self.queue.qsize() == 1:
            self.front = None
        self.size -= 1
        return self.queue.get()

    def top(self) -> int:
        return self.front

    def empty(self) -> bool:
        return not self.size


if __name__ == '__main__':
    my_stack = MyStack()
    my_stack.push(1)
    my_stack.push(2)
    print(my_stack.top())
    print(my_stack.pop())
    print(my_stack.empty())
