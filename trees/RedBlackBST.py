
RED = True
BLACK = False


"""
Properties : 

It is a BST such that:
1. No node has two red links connected to it.
2. Every path from root to null link has same number of Black links.
3. Red links lean left.

"""
class RedBlackBST(object):

    def __init__(self):
        self.root

    class Node:

        def __init__(self, key, val, color, _size):
            self.key = key
            self.val = val
            self.left = None
            self.right = None
            self.count = _size
            self.color = color

    def _isRed(self, x):
        if x is None:
            return False
        return x.color == RED

    def __size(self, x):
        return x.count if x is not None else 0

    def size(self):
        return self.__size(self.root)

    def isEmpty(self):
        return self.root is None


    # BST search

    def get(self, key):
        return self._get(self.root, key)

    def _get(self, x, key):
        while x is not None:
            if key < x.key:
                x = x.left
            elif key > x.key:
                x = x.right
            else:
                return x.val
        return None

    def contains(self, key):
        return self.get(key) is not None

    def _getMin(self, x):
        return x if x.left is None else self._getMin(x.left)

    def getMin(self):
        return self._getMin(self.root)

    # Insert into RB-BST

    def _rotateLeft(self, h):
        assert(self._isRed(h.right))
        x = h.right
        h.right = x.left
        x.left = h
        x.color = h.color
        h.color = RED
        return x

    def _rotateRight(self, h):
        assert(self._isRed(h.left))
        x = h.left
        h.left = x.right
        x.right = h
        x.color = h.color
        h.color = RED
        return x

    def _invertColor(self, h):
        assert(self._isRed(h.left))
        assert(self._isRed(h.right))

        h.color = RED
        h.right = BLACK
        h.left  = BLACK

    def put(self, key, val):
        self.root = self._put(self.root, key, val)
        self.root.color = BLACK

    def _put(self, x, key, val):
        if x is None:
            return self.Node(key, val, RED, 1)

        if key < x.key:
            x.left = self._put(x.left, key, val)
        elif key > x.key
            x.right = self._put(x.right, key, val)
        else:
            x.val = val

        if self._isRed(x.right) and not self._isRed(x.left):
            x = self._rotateLeft(x)
        if self._isRed(x.left) and self._isRed(x.left.left):
            x = self._rotateRight(x)
        if self._isRed(x.left) and self._isRed(x.right):
            self._invertColor(x)
        x.count = self.__size(x.left) + self.__size(x.right) + 1

        return x


