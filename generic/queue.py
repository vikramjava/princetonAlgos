""" Stack class"""

class Queue(object):


    class _node(object):

        def __init__(self, item, next):
            self.item = item
            self.next = next

    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def isEmpty(self):
        return (self.first is None)

    def enqueue(self, item):
        oldLast =  self.last
        self.last = self._node(item, None)
        if self.isEmpty():
            self.first = self.last
        else:
            oldLast.next = self.last
        self.size += 1

    def dequeue(self):
        giveFirst = self.first
        self.first = self.first.next
        self.size -= 1
        if self.isEmpty():
            self.last = None
        return giveFirst.item

    def total_size(self):
        return self.size


if __name__ == "__main__":
    curStack = Queue()
    for i in range(0, 30):
        curStack.enqueue(i)
    print curStack.total_size()
    while (curStack.isEmpty() is False):
        print curStack.dequeue()
