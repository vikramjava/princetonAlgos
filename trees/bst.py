

class BST(object):

    class _node(object):

        def __init__(self, key, val, N):
            self.key = key
            self.val = val
            self.N = N
            self.left = None
            self.right = None


    def __init__(self):
        self.root = None

    def isEmpty(self):
        return self.size() == 0

    def size(self):
        return self._size(self.root)

    def _size(self, x):
        return x.N if x is not None else 0

    def get(self, key):
        x = self.root
        while x is not None:
            if key == x.key  : return x.val
            elif key < x.key : x = x.left
            else             : x = x.right
        return None

    def put(self, key, value):
        if key is None:
            raise Exception("Valid key needs to be provided")

        self._root = self._put(self.root, key, value)

    def _put(self, x, key, val):
        if x is None:
            return self._node(key, val, N=1)

        if key == x.key: x.val    = val
        elif key < x.key: x.left  = self._put(x.left,  key, val)
        else:             x.right = self._put(x.right, key, val)
        x.N = 1 + self._size(x.left) + self._size(x.right)
        return x
    