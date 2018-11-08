
from vertex import *

class Graph:

    def __init__(self):
        self.vertList = []
        self.numVertices = 0

    def addVertex(self,v):
        self.numVertices = self.numVertices + 1
        self.vertList.append(v)

    #def getVertex(self,n):
    #    if n in self.vertList:
    #        return self.vertList[n]
    #    else:
    #        return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t):
        f.addNeighbor(t)
        t.addNeighbor(f)

    def getVertices(self):
        return self.vertList

    def __iter__(self):
        return iter(self.vertList.values())

    def existDominant(self,opponnents):
        for o in opponnents:
            if len(o.connectedTo) == 0:
                return False
        return True
