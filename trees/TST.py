

class TST(object):

    class node(object):

        def __init__(self, c):
            self.c = c
            self.left = None
            self.mid = None
            self.right = None
            self.val = None


    def __init__(self):
        self.count = 0
        self.root = None

    def size(self):
        return self.count

    def contains(self, key):
        return self.get(key)

    def get(self, key):
        if key is None:
            raise Exception ("Invalid Key")

        x = self._get(self.root, key, 0)
        if x is None:
            return None
        return x.val

    def _get(self, x, key, d):
        if x is None:
            return None
        c = key.charAt(d)
        if c < x.c:
            return self._get(x.left, key, d)
        elif c > x.c:
            return self._get(x.right, key, d)
        elif d < len(key) - 1:
            return self._get(x.mid, key, d+1)
        else:
            return x

    def put(self, key, val):
        if not self.contains(key):
            self.count += 1
        self.root = self._put(self.root, key, val, 0)

    def _put(self, x, key, val, d):
        c = key.charAt(d)
        if x is None:
            x = self.node(c)
        if c < x.c:
            x.left = self._put(x.left, key, val, d)
        elif c > x.c:
            x.right = self._put(x.right, key, val, d)
        elif d < len(key) - 1:
            x.mid = self._put(x.mid, key, val, d+1)
        else:
            x.val = val
        return x

