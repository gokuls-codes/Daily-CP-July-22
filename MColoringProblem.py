#User function Template for python3


#Function to determine if graph can be coloured with at most M colours such
#that no two adjacent vertices of graph are coloured with same colour.
def graphColoring(graph, k, V):
    
    #your code here
    colors = [-1 for _ in range(V)]

    print(color_graph(colors, graph, k,V, 0))
    print(colors)
    
    return color_graph(colors, graph, k,V, 0)

def color_graph(colors, graph, k, V, s):
    if s >= V:
        return True
    for c in range(k):
        if is_valid(colors, c, graph, s):
            colors[s] = c
            if color_graph(colors, graph, k, V, s+1) :
                return True

        colors[s] = -1

    return False

def is_valid(colors, c, graph, v):
    for i in range(len(graph)):
        if graph[v][i] == 1 and colors[i] == c:
            return False

    return True