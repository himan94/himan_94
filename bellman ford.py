import sys

class graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self,name,edges):
        self.vertices[name] = edges

    def bell(self,start):
        distances = {}
        pred = {}

        for vert in self.vertices:
            for j in self.vertices[vert]:
                if vert == start or j == start:
                    distances[vert] = 0
                else:
                    distances[j] = sys.maxsize
                    distances[vert] = sys.maxsize
        

        l = 0
        while l<3:
            for vert1 in self.vertices:
                for j1 in self.vertices[vert1]:
                    if distances[vert1] == sys.maxsize and distances[j1] == sys.maxsize :#if distances of both vertex of edge is 0 dont consider
                        distances[j1] = sys.maxsize # keep distance = infinity
                    elif distances[vert1] + self.vertices[vert1][j1] < distances[j1]: #if new path calculated is lesser than the path in previous iteration
                        distances[j1] = distances[vert1] + self.vertices[vert1][j1]  
                        pred[j1] = [vert1]
            l = l+1
            print distances
            print pred
            
g = graph()
g.add_vertex('A', {'C': 3})
g.add_vertex('B', {'A':-5,'D': 1})
g.add_vertex('C', {'D': 2})
g.add_vertex('S', {'A':4,'B':6})
print g.bell('S')
