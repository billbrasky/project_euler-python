data = """
By starting at the top of the triangle below and moving to adjacent numbers on 
the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by 
trying every route. However, Problem 67, is the same challenge with a triangle 
containing one-hundred rows; it cannot be solved by brute force, and requires a 
clever method! ;o)
"""

import heapq

class SquareGrid:
    def __init__( self, data):
        
        self.width = len( data[-2] )
        self.height = len( data )
        self.data = data
        self.walls = []
    
    def in_bounds(self, id):
        (x, y) = id
        h = self.height
        w = self.width
        
        return 0 <= x < h and 0 <= y < w #and x+y <= h
    
    def passable(self, id):
        return id not in self.walls
    
    def neighbors(self, id):
        (x, y) = id
        results = [(x,y+1),(x+1,y)]#[(x+1, y), (x, y-1),(x, y-1), (x, y+1)]
#        if x == self.height - 2:
#            results = [(self.height-1,0), (x,y+1)]
#        else:
        if (x + y) % 2 == 0: results.reverse() # aesthetics
        results = filter(self.in_bounds, results)
#        results = filter(self.passable, results)
        return results

class GridWithWeights(SquareGrid):
    def __init__(self, data):
        super().__init__(data)

        self.weights = {}
        
        for h in range( self.height ):
#            print( self.data[h])
            for w in range( len( self.data[h] )):
                
                self.weights[(h, w)] = int( self.data[h][w] )
                
            
    
    def cost(self, from_node, to_node):
        cost = self.weights.get(to_node, 0)#+self.weights.get(from_node, 0)
#        print( from_node, to_node, cost)
        return cost

class PriorityQueue:
    def __init__( self ):
        self.elements = []
    
    def empty( self ):
        return len( self.elements ) == 0
    
    def put( self, item, priority ):
        heapq.heappush( self.elements, ( priority, item ))
    
    def get( self ):
        return heapq.heappop( self.elements )[1]

def heuristic( a, b, graph ):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)

def a_star_search( graph, start, goal ):
    frontier = PriorityQueue()
    frontier.put( start, 0 )
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = graph.weights[start]
    print( frontier.elements, frontier.empty() )
    while not frontier.empty():
        current = frontier.get()
        print( current )
        if current == goal:
            break
#        print( 'd',current, list(graph.neighbors( current )))
        for next in graph.neighbors( current ):
            new_cost = cost_so_far[current] + graph.cost( current, next )
            if next not in cost_so_far or new_cost > cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = 0#new_cost * heuristic( goal, next, graph )
                frontier.put( next, priority )
                came_from[next] = current
    
    return came_from, cost_so_far
def reconstruct_path(came_from, start, goal):
    current = goal
    path = []
    while current != start:
        print( current )
        path.append(current)
        current = came_from[current]
    path.append(start) # optional
    path.reverse() # optional
    return path

def from_id_width(id, width):
    return (id % width, id // width)

def draw_tile(graph, id, style, width):
    r = "."
    if 'number' in style and id in style['number']: r = "%d" % style['number'][id]
    if 'point_to' in style and style['point_to'].get(id, None) is not None:
        (x1, y1) = id
        (x2, y2) = style['point_to'][id]
        if x2 == x1 + 1: r = ">"
        if x2 == x1 - 1: r = "<"
        if y2 == y1 + 1: r = "v"
        if y2 == y1 - 1: r = "^"
    if 'start' in style and id == style['start']: r = "A"
    if 'goal' in style and id == style['goal']: r = "Z"
    if 'path' in style and id in style['path']: r = "@"
    if id in graph.walls: r = "#" * width
    return r

def draw_grid(graph, width=2, **style):
    for x in range(graph.height):
        for y in range(graph.width):
#            if x == 0 and y > 0: break
#            if y+x <= 4:
            print("%%-%ds" % width % draw_tile(graph, (x, y), style, width), end="")
        print()

#data = data.split( '\n' )[13:-6]
#data = [x.split( ' ' ) for x in data] + [[1]]
#data = [
#    [3],
#    [7, 4],
#    [2, 4, 6],
#    [8, 5, 9, 3]
#]
data = data.split( '\n' )[13:-6]
print( data )
data = [x.split( ' ' ) for x in data]
i = -1
m = len( data )
newdata = []
while i >= -m:
    x = [data[y][i] for y in range( abs(i)-1, m )] + [0]*( abs(i)-1)
    newdata.append( x )
    i -= 1

data = newdata
from pprint import pprint

g = GridWithWeights( data)


start, goal = (0, 0), (len(data)-1, len( data ) -1)

cf, cost = a_star_search( g, start, goal )

draw_grid(g,width=10,path=reconstruct_path(cf,start, goal))


