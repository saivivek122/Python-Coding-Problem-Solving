class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)

    def dfs(self, vertex):

        visited = [vertex]
        stack = [vertex]
        while stack:
            pop_vertex = stack.pop()
            print(pop_vertex)
            for adjacent_vertex in self.gdict[pop_vertex]:
                if adjacent_vertex not in visited:
                    visited.append(adjacent_vertex)
                    stack.append(adjacent_vertex)


custom_dict = {"a": ["b", "c"],
               "b": ["a", "d", "e"],
               "c": ["a", "e"],
               "d": ["b", "e", "f"],
               "e": ["d", "f", "c", "b"],
               "f": ["d", "e"]}
graph = Graph(custom_dict)
graph.dfs("a")
