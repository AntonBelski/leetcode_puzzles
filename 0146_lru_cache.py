from collections import defaultdict, deque


class Node:
    def __init__(self, key, val, prev=None, nexxt=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.nexxt = nexxt


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, key, val):
        if not self.head:
            self.head = self.tail = Node(key, val)
        else:
            self.tail.nexxt = Node(key, val, prev=self.tail)
            self.tail = self.tail.nexxt
        return self.tail

    def delete(self, node):
        if self.head == self.tail:
            self.head = self.tail = None
        elif self.head == node:
            self.head = node.nexxt
            self.head.prev = None
        elif self.tail == node:
            self.tail = node.prev
            self.tail.nexxt = None
        else:
            node.prev.nexxt = node.nexxt
            node.nexxt.prev = node.prev
        return node.key, node.val


class LRUCache:
    # My second optimized solution (checked tag in solutions - Doubly Linked List)
    # Time - O(1), Space = O(c), where c - capacity
    def __init__(self, capacity: int):
        self.dlist = DoublyLinkedList()
        self.cache = defaultdict(int)
        self.max_size = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            key, val = self.dlist.delete(self.cache[key])
            self.cache[key] = self.dlist.add(key, val)
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            if self.dlist.tail.key == key:
                self.cache[key].val = value
                return
            self.dlist.delete(self.cache[key])
        elif self.max_size == len(self.cache):
            del self.cache[self.dlist.head.key]
            self.dlist.delete(self.dlist.head)
        self.cache[key] = self.dlist.add(key, value)


class LRUCache2:
    # My first solution, correct complexity for the problem constraints (O(1) in average for time), but not optimal
    # Time - O(1) in average, Space = O(m), where m - number of all operations
    def __init__(self, capacity: int):
        self.cache = {}
        self.cache_freq = defaultdict(int)
        self.max_size = capacity
        self.deq = deque()

    def get(self, key: int) -> int:
        if key in self.cache:
            self.deq.append(key)
            self.cache_freq[key] += 1
        return self.cache.get(key, -1)

    def put(self, key: int, value: int) -> None:
        if self.max_size == len(self.cache) and key not in self.cache:
            while self.cache_freq[self.deq[0]] != 1:
                self.cache_freq[self.deq.popleft()] -= 1
            del self.cache_freq[self.deq[0]]
            del self.cache[self.deq.popleft()]

        self.deq.append(key)
        self.cache_freq[key] += 1
        self.cache[key] = value


if __name__ == '__main__':
    capacity = 2
    lRUCache = LRUCache(capacity)
    lRUCache.put(1, 1)
    lRUCache.put(2, 2)
    print(lRUCache.get(1))
    lRUCache.put(3, 3)
    print(lRUCache.get(2))
    lRUCache.put(4, 4)
    print(lRUCache.get(1))
    print(lRUCache.get(3))
    print(lRUCache.get(4))
    print()

    lRUCache2 = LRUCache2(capacity)
    lRUCache2.put(1, 1)
    lRUCache2.put(2, 2)
    print(lRUCache2.get(1))
    lRUCache2.put(3, 3)
    print(lRUCache2.get(2))
    lRUCache2.put(4, 4)
    print(lRUCache2.get(1))
    print(lRUCache2.get(3))
    print(lRUCache2.get(4))
    print()
