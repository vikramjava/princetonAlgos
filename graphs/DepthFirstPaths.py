import collections as cx

class DepthFirstPaths(object):

    def __init__(self, G, s):
        self.s = s
        self.edgeTo = cx.OrderedDict([(v, None) for v in G.keys])
        self.marked = cx.OrderedDict([(v, False) for v in G.keys])
        self._dfs(G, s)

    def _dfs(self, G, v):
        self.marked[v] = True
        for w in G.adj(v):
            if not self.marked[w]:
                self.edgeTo[w] = v
                self._dfs(G, w)

    def hasPathTo(self, v):
        return self.marked[v]

    def pathTo(self, v):
        if not self.hasPathTo(v):
            return None

        path = []
        x = v
        while x != self.s:
            path.append(x)
            x = self.edgeTo[x]
        path.append(self.s)
        return path
