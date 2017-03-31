class Vertex:
    def __init__(self,v):

        self.name = v
        self.neighbor = list()

        self.color = "black"
        self.distance = 999

    def add_neighbor(self,vert):
        if vert not in self.neighbor:
            self.neighbor.append(vert)
            self.neighbor.sort()

class graph:

    vertices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
        else:
            return False
    
    def add_edge(self,u,v):

        if u in self.vertices and v in self.vertices:
            for key,value in self.vertices.items():
                if key==u:
                    value.add_neighbor(v)
                if key==v:
                    value.add_neighbor(u)
            return True
        else:
            print False

    def print_v(self):
        for key in self.vertices.keys():
            print(str(key) + str(self.vertices[key].neighbor) + "  " + str(self.vertices[key].distance))

    def bfs(self,ver):
        q = list()
        ver.color="red"
        ver.distance = 0
        q.append(ver)
        while len(q)> 0:
            a = q.pop(0)
            for l in a.neighbor:
                node_v = self.vertices[l]
                if node_v.color == "black":
                    node_v.distance = a.distance+1
                    q.append(node_v)               
                    node_v.color = "red"
                
                    
g = graph()
a = Vertex('A')
g.add_vertex(a)
#g.add_vertex(Vertex('B'))
for i in range(ord('A'), ord('L')):
	g.add_vertex(Vertex(chr(i)))

edges = ['AB', 'AE', 'BF', 'BC', 'EI', 'FG','IF', 'GJ', 'GK', 'KH', 'HD']
for edge in edges:
	g.add_edge(edge[:1], edge[1:])
	
g.bfs(a)
g.print_v()
