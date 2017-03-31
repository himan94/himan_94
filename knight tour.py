from pythonds.graphs import Graph

def knightGraph(bds):
    g = Graph()
    for row in range(bds):
        for col in range(bds):
            hull = gennumb(row,col,bds)
            node1 = genLegalMoves(row,col,bds)
            for j in node1:
                g.addEdge(hull,j)
    return g


def gennumb(rows,columns,board_size):
    return (rows*board_size)+columns

def genLegalMoves(row1,col1,bdsize):
    
    possmov = []
    moveOffsets = [(-1,-2),(-1,2),(-2,-1),(-2,1),
                   ( 1,-2),( 1,2),( 2,-1),( 2,1)]
    for i in moveOffsets:
        newr = row1 + i[0]
        newc = col1 + i[1]
        z = gennumb(newr,newc,bdsize)
        if z >=0 and z < 25 :
            possmov.append(z)
        else:
            print"out of board"

    return possmov

y = int(raw_input("enter a number below or equal to 8"))
l = knightGraph(y)    
for v in l:
    for w in v.getConnections():
        if (v.getId()/y)*y < w.getId()<((v.getId()/y)+1)*y:
            print"not possible"
        else:    
            print("( %s , %s )" % (v.getId(), w.getId()))

