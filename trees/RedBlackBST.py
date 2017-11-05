

class RedBlackBST(object):

    RED   = True
    BLACK = False

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
            elif key > x.key
                x = x.right
            else:
                return x.val
        return None

    def contains(self, key):
        return self.get(key) is not None



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
        
