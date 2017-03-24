import heapq
import sys

class Graph:
    
    def __init__(self):
        self.vertices = {}
        
    def add_vertex(self, name, edges):
        self.vertices[name] = edges
    
    def shortest_path(self, start, finish):
        distances = {} # Distance from start to node
        previous = {}  # Previous node in optimal path from source
        nodes = [] # Priority queue of all nodes in Graph

        for vertex in self.vertices:
            if vertex == start: # Set root node as distance of 0
                distances[vertex] = 0
                heapq.heappush(nodes, [0, vertex])
            else:
                distances[vertex] = sys.maxsize
                heapq.heappush(nodes, [sys.maxsize, vertex])
            previous[vertex] = None

        smallest = heapq.heappop(nodes)[1]
        i=0
        while i<4:
            l=[]    
            m=[]    
            for neighbor in self.vertices[smallest]: # Look at all the nodes that this vertex is attached to
                if distances[neighbor]>distances[smallest]:
                    alt = distances[smallest] + self.vertices[smallest][neighbor]# Alternative path distance
                    alt1 = min(distances[neighbor],alt)
                    distances[neighbor] = alt1
                    l.append(neighbor)
                    m.append(alt1)
            s = min(m)
            t = m.index(s)
            u = l[t]
            smallest = u
            for p in range(len(l)):
                l.pop()
                m.pop()
            print distances    
            i = i+1
        return max(distances.values())   

g = Graph()
g.add_vertex('A', {'B': 10, 'C': 5})
g.add_vertex('B', {'A':10,'C': 8, 'D': 12, 'E':6})
g.add_vertex('C', {'A':10,'B': 8, 'E': 12})
g.add_vertex('D', {'B':12, 'E': 12,'F':4})
g.add_vertex('E', {'C':12,'B': 6,'D':5,'F':6})
g.add_vertex('F', {'D': 4, 'E': 6})

print (g.shortest_path('A', 'F'))    
"""                
g = Graph()
    g.add_vertex('A', {'B': 7, 'C': 8})
    g.add_vertex('B', {'A': 7, 'F': 2})
    g.add_vertex('C', {'A': 8, 'F': 6, 'G': 4})
    g.add_vertex('D', {'F': 8})
    g.add_vertex('E', {'H': 1})
    g.add_vertex('F', {'B': 2, 'C': 6, 'D': 8, 'G': 9, 'H': 3})
    g.add_vertex('G', {'C': 4, 'F': 9})
    g.add_vertex('H', {'E': 1, 'F': 3})
    print(g.shortest_path('A', 'H'))
    """
