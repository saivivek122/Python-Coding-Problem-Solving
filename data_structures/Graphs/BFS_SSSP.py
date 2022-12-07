class Graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = {}

    def addEdge(self,vertex,edge):
        self.gdict[vertex].append(edge)



