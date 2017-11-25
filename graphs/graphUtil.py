
import collections

def adjListToArr(adjList):
    return adjOrderedDictToEVpairs_UD(adjListToOrdredDict(adjList))

def adjListToOrdredDict(adjList):
    lst = []
    for line in adjList.splitlines():
        line = line.strip()
        if line:
            lst.append(_adjstr2arr(line))
    return collections.OrderedDict(lst)

def adjOrderedDictToEVpairs_UD(od):
    V = len(od)
    v2i = {v:i for i, v in enumerate(od.keys())}
    i2v = {i:v for v2i.items()}
    edges = set([tuple(sorted([v2i[a], v2i[b]])) for a, bs in od.items() for b in bs])
    a = [V, len(edges)] + list(edges)
    return a, i2v

def _adjstr2arr(adjstr):
  """Convert "A:  F B E" to ('A', ('F', 'B', 'E'))."""
  M = re.search(r'^(\S+)\s*:\s*(\S.*)$', adjstr)
  if M:
    return (M.group(1), M.group(2).split())
  raise Exception("NO ADJACENCY LIST FOUND IN({})".format(adjstr))
