import sys

class Graph:
    
    def __init__(self):
        self.vertices = {}
        
    def add_vertex(self, name, edges):
        self.vertices[name] = edges

    def conv(self,v):

        if v=='A':
            return 0
        elif v =='B':
            return 1
        elif v=='C':
            return 2
        elif v =='D':
            return 3
        elif v=='E':
            return 4
        elif v =='F':
            return 5
        elif v ==0:
            return 'A'
        elif v ==1:
            return 'B'
        elif v ==2:
            return 'C'
        elif v ==3:
            return 'D'
        elif v ==4:
            return 'E'
        elif v==5:
            return 'F'
  
    def mst(self,start):
        matrix = []
        path= []
        distance=[]
        b = len(self.vertices)

        for i in range((b)):                       #create a matrix of rows = no of vertices
            matrix.append(["X"]*b)                 # and cloumns = no of vertices
                                
        for l in self.vertices:                    # assinging the weight to the matrix 
            for p in self.vertices[l]:
                matrix[self.conv(l)][self.conv(p)] = self.vertices[l][p]
                
        for u in range(b):                          #the weights which are zero are assigned infinity
            for v in range(b):
                if matrix[u][v] == 'X':
                    matrix[u][v] = sys.maxsize

        u = 0
        z = self.conv(start)
        while u < b-1:

            v = min(matrix[z])                    #min of a row
            w = matrix[z].index(v)                #index of the row which also tells us the alphabet
            distance.append(v)                    
            path.append(str(self.conv(z))+str(self.conv(w)))
            matrix[z][w] = sys.maxsize
            matrix[w][z] = sys.maxsize
            u = u+1
            z = w

        print distance
        print" sum is %d"%(sum(distance))
        return path    
            
g = Graph()
g.add_vertex('A', {'C': 5,'B': 10})
g.add_vertex('B', {'A':10,'C': 8, 'D': 12, 'E':6})
g.add_vertex('C', {'A':10,'B': 8, 'E': 12})
g.add_vertex('D', {'B':12, 'E': 12,'F':4})
g.add_vertex('E', {'C':12,'B': 6,'D':5,'F':6})
g.add_vertex('F', {'D': 4, 'E': 6})

print g.mst('A')

            
