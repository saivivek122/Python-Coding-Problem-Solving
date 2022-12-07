class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)

    def bfs(self, vertex):
        visited = [vertex]
        
        queue = [vertex]
        while queue:
            de_vertex = queue.pop(0)
            print(de_vertex)
            for adjacencyVertex in self.gdict[de_vertex]:
                if adjacencyVertex not in visited:
                    visited.append(adjacencyVertex)
                    queue.append(adjacencyVertex)


custom_dict = {"a": ["b", "c"],
               "b": ["a", "d", "e"],
               "c": ["a", "e"],
               "d": ["b", "e", "f"],
               "e": ["d", "f", "c", "b"],
               "f": ["d", "e"]}
graph = Graph(custom_dict)
graph.bfs("a")
