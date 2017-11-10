

class RTrie(object):
    R = 256

    class Node(object):

        def __init__(self):
            self.val
            self.next = [None for i in range(RTrie.R)]

    def __init__(self):
        self.root = self.Node()  # Root of trie
        self.count


    # Search operations

    def _get(self, x, key, d):
        if x is None:
            return None

        if d == len(key):
            return x

        c = key.charAt(d)
        return self._get(x.next[c], key, d+1)

    def get(self, key):
        x = self._get(self.root, key, 0)
        if x is None:
            return None
        return x.val

    def contains(self, key):
        return self.get(key) is not None


    # Insert operations

    def _put(self, x, key, val, d):

        # Create a new Node if one is not present.
        if x is None:
            x = self.Node

        # Once we have matched the key, update the value and return
        if d == len(key):
            x.val = val
            return x

        # Keep adding new Nodes until we reach the length of the key
        c = key.charAt(d)
        x.next[c] = self._put(x.next[c], key, val, d+1)
        return x

    def put(self, key, val):
        self.root = self._put(self.root, key, val, 0)

    