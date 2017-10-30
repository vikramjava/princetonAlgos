

class queueResizingArray:

    def __init__(self):
        self.queue = [None, None]
        self.size = 0
        self.first = 0
        self.last = 0

    def isEmpty(self):
        return self.size == 0

    def totalSize(self):
        return self.size

    def capacity(self):
        return len(self.queue)

    def resize(self, capacity):
        assert capacity >= self.size
        tq = [None for _ in xrange(capacity)]
        curr_capacity = self.capacity()
        for i in xrange(self.size):
            tq[i] = self.queue[(self.first + i) % curr_capacity]
        self.queue = tq
        self.first = 0
        self.last = self.size

    def enqueue(self, item):
        if self.totalSize() == self.capacity():
            self.resize(2 * self.capacity())
        self.queue[self.last] = item
        self.last += 1
        if self.last == self.capacity():
            self.last = 0
        self.size += 1

    def dequeue(self):
        item = self.queue[self.first]
        self.queue[self.first] = None
        self.size -= 1
        self.first += 1
        if self.first == self.capacity():
            self.first = 0

        if self.totalSize() > 0 and self.size == self.capacity()/4:
            self.resize(self.capacity()/2)
        return item
