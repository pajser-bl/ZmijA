


#prepisano sa:
# https://en.wikipedia.org/wiki/A*_search_algorithm#Pseudocode

class Node(object):
    def __init__(self,(x,y),parent):
        self.children=[]
        self.parent=parent
        if parent:
            self.path=parent.path[:]
    


def reconstruct_path(came_from, current):
    total_path = {current}
    while current in came_from:
        current = came_from[current]
        total_path.append(current)
    return total_path

#heuristika
def distance(T1,T2):
    (x1,y1)=T1
    (x2,y2)=T2
    return abs(x1-x2)+abs(y1-y2)

def a_star(start,goal):
    closed_set=[]
    opened_set={start}
    came_from=[]

def getAwailableNeigbours(T,matrix[][]):
    (x,y)=T
    if x-1>=0 || x+1<len(matrix) || matrix[x,y]!=2 || matrix[x,y]!=1

