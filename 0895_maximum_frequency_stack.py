from collections import defaultdict
from heapq import heappop, heappush


class FreqStack2:
    def __init__(self):
        self.heap = []
        self.counter = defaultdict(int)
        self.push_counter = 0

    def push(self, val: int) -> None:
        self.counter[val] += 1
        self.push_counter += 1
        heap_elem = [-self.counter[val], -self.push_counter, val]
        heappush(self.heap, heap_elem)

    def pop(self) -> int:
        pair = heappop(self.heap)
        val = pair[2]
        self.counter[val] -= 1
        return val


class FreqStack:
    def __init__(self):
        self.freq = defaultdict(int)
        self.group = defaultdict(list)
        self.max_freq = 0

    def push(self, val: int) -> None:
        self.freq[val] += 1
        self.group[self.freq[val]].append(val)
        self.max_freq = max(self.max_freq, self.freq[val])

    def pop(self) -> int:
        val = self.group[self.max_freq].pop()
        self.freq[val] -= 1

        if not self.group[self.max_freq]:
            self.max_freq -= 1

        return val


if __name__ == '__main__':
    freq_stack = FreqStack()
    freq_stack.push(5)
    freq_stack.push(7)
    freq_stack.push(5)
    freq_stack.push(7)
    freq_stack.push(4)
    freq_stack.push(5)
    print(freq_stack.pop())
    print(freq_stack.pop())
    print(freq_stack.pop())
    print(freq_stack.pop())
    print()
    freq_stack = FreqStack2()
    freq_stack.push(5)
    freq_stack.push(7)
    freq_stack.push(5)
    freq_stack.push(7)
    freq_stack.push(4)
    freq_stack.push(5)
    print(freq_stack.pop())
    print(freq_stack.pop())
    print(freq_stack.pop())
    print(freq_stack.pop())
