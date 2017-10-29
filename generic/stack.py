""" Stack class"""

class Stack(object):


    class _node(object):

        def __init__(self, item, next):
            self.item = item
            self.next = next

    def __init__(self):
        self.first = None
        self.size = 0

    def isEmpty(self):
        return (self.size == 0)

    def push(self, item):
        oldFirst = self.first
        self.first = self._node(item, oldFirst)
        self.size += 1

    def pop(self):
        giveFirst = self.first
        self.first = self.first.next
        self.size -= 1
        return giveFirst.item

    def size(self):
        return self.size

    def __str__(self):
        return ''.join([str(item) for item in self])

    def __repr__(self):
        return self.__str__()

