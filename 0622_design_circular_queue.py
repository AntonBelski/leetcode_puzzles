from typing import List


class MyCircularQueue:
    def __init__(self, k: int):
        self.head = -1
        self.tail = -1
        self.queue = [None] * k
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.size == len(self.queue):
            return False

        if self.tail == len(self.queue) - 1:
            self.tail = 0
        else:
            if self.head == -1:
                self.head += 1
            self.tail += 1

        if self.queue[self.tail] is None:
            self.queue[self.tail] = value
            self.size += 1
            return True

    def deQueue(self) -> bool:
        if self.size == 0:
            return False

        self.queue[self.head] = None
        self.size -= 1

        if self.size == 0:
            self.head = -1
            self.tail = -1
        elif self.head == len(self.queue) - 1:
            self.head = 0
        else:
            self.head += 1

        return True

    def Front(self) -> int:
        if self.size:
            return self.queue[self.head]
        else:
            return self.head

    def Rear(self) -> int:
        if self.size:
            return self.queue[self.tail]
        else:
            return self.tail

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == len(self.queue)


if __name__ == '__main__':
    my_circular_queue = MyCircularQueue(3)
    print(my_circular_queue.enQueue(1))
    print(my_circular_queue.enQueue(2))
    print(my_circular_queue.enQueue(3))
    print(my_circular_queue.enQueue(4))
    print(my_circular_queue.Rear())
    print(my_circular_queue.isFull())
    print(my_circular_queue.deQueue())
    print(my_circular_queue.enQueue(4))
    print(my_circular_queue.Rear())
