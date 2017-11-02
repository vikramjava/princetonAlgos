
import operator
import pprint

less = operator.lt

class maxPQ(object):

    def __init__(self):
        self.pq = []
        self.N = 0
        return

    def insert(self, x):
        self.pq.append(x)
        self.N += 1
        self._swim(self.pq, len(self.pq) - 1)
        return

    def delMax(self):
        max_val = self.pq[1]
        self.pq[0], self.pq[self.N-1] = self.pq[self.N-1], self.pq[0]
        self._sink(self.pq, 0)
        self.pq[self.N-1] = None
        del self.pq[self.N - 1]
        return max_val

    def isEmpty(self):
        return self.N == 0

    def max(self):
        return self.pq[0]

    def size(self):
        return self.N

    def _swim(self, a, k):
        while k > 0 and less(a[k/2], a[k]):
            a[k], a[k/2] = a[k/2], a[k]
            k = k/2

    def _sink(self, a, k):
        while (2 * k <= self.N):
            if k == 0:
                j = 1
            else:
                j = 2 * k

            # Find the larger of 2k and 2k + 1
            if j < self.N and less(j, j+1):
                j += 1
            if not less (k, j):
                break
            a[k], a[j] = a[j], a[k]
            k = j

    def __str__(self):
        pq_str = (" ").join(self.pq)
        return pq_str


if __name__ == "__main__":
    list = ['B', 'S', 'T', 'C', 'Q', 'A', 'Z']
    pq = maxPQ()
    for _ in list:
        pq.insert(_)
    print pq
