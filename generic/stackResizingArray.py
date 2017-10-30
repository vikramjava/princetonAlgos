
class stackResizingArray(object):

    def __init__(self):
        self.stack = [None, None]
        self.N = 0

    def isEmpty(self):
        return self.N == 0

    def size(self):
        return self.N

    def capacity(self):
        return len(self.stack)

    def push(self, item):
        if self.N == len(self.stack):
            self._resize(2*len(self.stack))
        self.stack[self.N] = item
        self.N += 1

    def pop(self):
        if self.isEmpty():
            raise Exception("Stack Underflow fatal error")
        item = self.stack[self.N - 1]
        self.N -= 1
        self.stack[self.N] = None
        if self.N > 0 and self.N == len(self.stack)/4:
            self.resize(len(self.stack)/2)
        return item

    def _resize(self, new_capacity):
        tarr = [None for i in range(new_capacity)]
        for i in range(self.N):
            tarr[i] = self.stack[i]
        self.stack = tarr


if __name__ == "__main__":
    curStack = stackResizingArray()
    for i in range(0, 34):
        print("Capacity is " + str(curStack.capacity()))
        curStack.push(i)
    print curStack.size()
    print curStack.pop()