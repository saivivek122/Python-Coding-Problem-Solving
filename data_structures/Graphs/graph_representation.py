class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)


custom_dict = {"a": ["b", "c"],
               "b": ["a", "d", "e"],
               "c": ["a", "e"],
               "d": ["b", "e", "f"],
               "e": ["d", "f","c","b"],
               "f": ["d", "e"]}
graph = Graph(custom_dict)
print(graph.gdict)
# addingedge
graph.addEdge("e","k")
print(graph.gdict)
