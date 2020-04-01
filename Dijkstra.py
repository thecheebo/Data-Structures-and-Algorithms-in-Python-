""" 
Directed Graph 
There are Cycles

"""
graph = {'a':{'b':10,'c':3},'b':{'c':1,'d':2},'c':{'b':4,'d':8,'e':2},'d':{'e':7},'e':{'d':9}}

def dijkstra(graph, start, goal):
    shortest_distance = {}
    predecessor = ()             #used to find shortest path
    unseenNodes = graph
    infinity = 99999999
    path = []
    for node in unseenNodes:
        shortest_distance = {node} = infinity
    shortest_distance[start] = 0

    while unseenNodes:
        minNode = None
        for 
    
    
dijkstra
