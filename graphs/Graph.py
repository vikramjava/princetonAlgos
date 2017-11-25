

class Graph(object):

    def __init__(self, a=None):
        if a is not None:
            if isInstance(a, int):
                self._init_empty(a)
            elif len(a) == 1:
                self._init_empty(a[0])
            else:
                self._init(a)
            self.keys = range(self._v)

        '''
        elif 'adjtxt' in kwargs:
            self._adj = adjListToOrdredDict(kwargs['adjtxt'])
            self._V = len(self._adj)
            self._E = len(set([tuple(sorted([v, w])) for v, ws in self._adj.items() for w in ws]))
            self.keys = self._adj.keys()
        '''

    def _init_empty(self, V):
        if V < 0:
            raise Exception("Number of vertices must be positive")
        self._V = V
        self._E = 0
        self._adj = [set() for v in range(V)]

    def _init(self, a):
        self._init_empty(a[0])
        E = a[1]
        if E < 0:
            raise Exception("Number of edges must be positive")

        for v, w in a[2:]:
            self.addEdge(v, w)

    def addEdge(v, w):
        self._E += 1
        self._adj[v].add(w)
        self._adj[w].add(v)

    def V():
        return self._V

    def E():
        return self._E

    def adj(self, v):
        return self._adj[v]

    def degree(self, v):
        return self._adj[v].size()

    def __str__(self):
        s = [(("{V} vertices, {E} edges\n").format(V=self.V(). E=self.E()))]
        for v in self.keys:
            s.append("{v} : ".format(v=v))
            for w in self._adj[v]:
                s.append("{w} ".format(w=w))
            s.append("\n")
        return ''.join(s)

    def __iter__(self):
        return iter(self._adj)

    def get_edges(self):
        edges = set()
        for v in self.keys:
            for w in self._adj[v]:
                edges.add(tuple(sorted([v, w])))
        return edges
