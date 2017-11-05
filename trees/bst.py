

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

    def _get_min(self, x):
        return x if x.left is None else self._get_min(x.left)

    def get_min(self):
        if self.isEmpty():
            raise Exception("Trying to get a minimum from an empty tree")
        return self._get_min(self.root)

    def _get_max(self, x):
        return x if x.right is None else self._get_max(x.right)

    def get_max(self):
        if self.isEmpty():
            raise Exception("Trying to get a maximum from an empty tree")
        return self._get_max(self.root)

    def _floor(self, x, key):
        if x is None:
            return None
        if key == x.key:
            return x
        if key < x.key:
            return self._floor(x.left, key)
        t = self._floor(x.right, key)
        return t if t is not None else return x

    def __floor__(self, key):
        if key is None: raise Exception("Provided Key is None")
        if self.isEmpty(): "Current BST is empty"
        x = self._floor(self.root, key)
        return x.key if x is not None else None

    def _ceil(self, x, key):
        if x is None:
            return None
        if key == x.key:
            return x
        if key < x.key:
            t = self._ceil(x.left, key)
            return t if t is not None else x
        return self._ceil(x.right, key)

    def ceil(self, key):
        x = self._ceil(self.root, key)
        return x if x is not None else key

    def _rank(self, x, key):
        if x is None:
            return 0
        if key < x.key:
            return self._rank(x.left, key)
        elif key > x.key:
            return 1 + self._size(x.left) + self._size(x.right)
        else:
            return self._size(x.left)

    def rank(self, key):
        return self._rank(self.root, key)

    def _deleteMin(self, x):
        if x.left is None:
            return x.right
        x.left = self._deleteMin(x.left)
        x.N = 1 + self._size(x.left) + self._size(x.right)
        return x

    def deleteMin(self):
        self.root = self._deleteMin(self.root)

    def _deleteMax(self, x)
        if x.right is None:
            return x.left
        x.right = self._deleteMax(x.right)
        x.N = 1 + self._size(x.left) + self._size(x.right)
        return x

    def deleteMax(self, x):
        self.root = self._deleteMax(self.root)


