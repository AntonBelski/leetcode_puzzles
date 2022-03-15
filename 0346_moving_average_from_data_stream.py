class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        self.sum = 0

    def add_tail(self, val):
        new_tail = ListNode(val)
        if not self.tail:
            self.head = self.tail = new_tail
        else:
            self.tail.next = new_tail
            self.tail = new_tail
        self.size += 1
        self.sum += val

    def remove_head(self):
        self.sum -= self.head.val
        if self.tail == self.head:
            self.tall = self.head = None
        else:
            self.head = self.head.next
        self.size -= 1


class MovingAverage:
    def __init__(self, size: int):
        self.max_size = size
        self.linked_list = LinkedList()

    def next(self, val: int) -> float:
        self.linked_list.add_tail(val)

        if self.linked_list.size > self.max_size:
            self.linked_list.remove_head()

        return self.linked_list.sum / self.linked_list.size


if __name__ == '__main__':
    moving_average = MovingAverage(3)
    print(moving_average.next(1))
    print(moving_average.next(10))
    print(moving_average.next(3))
    print(moving_average.next(5))
