from collections import deque


class HitCounter:
    def __init__(self):
        self.deque = deque()
        self.last_hits = 0

    def hit(self, timestamp: int) -> None:
        self.deque.append(timestamp)
        self.last_hits += 1

        while timestamp - 300 >= self.deque[0]:
            self.last_hits -= 1
            self.deque.popleft()

    def getHits(self, timestamp: int) -> int:
        while self.deque and timestamp - 300 >= self.deque[0]:
            self.last_hits -= 1
            self.deque.popleft()

        return self.last_hits


if __name__ == '__main__':
    hit_counter = HitCounter()
    hit_counter.hit(1)
    hit_counter.hit(2)
    hit_counter.hit(3)
    print(hit_counter.getHits(4))
    hit_counter.hit(300)
    print(hit_counter.getHits(300))
    print(hit_counter.getHits(301))
