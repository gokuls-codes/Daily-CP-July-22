#User function Template for python3

class Solution:
    # Function to construct and return cost of MST for a graph
    # represented using adjacency matrix representation
    '''
    V: nodes in graph
    adj: adjacency list for the graph
    S: Source
    '''
    def bellman_ford(self, V, adj, S):
        #code here
        distance = [100000000] * V
        distance[S] = 0
        print(distance)
        
        for i in range(V - 1):
            for u, v, weight in adj:
                if distance[u] != float("Inf") and distance[u] + weight < distance[v]:
                    distance[v] = distance[u] + weight
                print(u, v, weight, distance)
                    
        return distance

print(Solution().bellman_ford(3,[[0,1,5],[1,0,3],[1,2,-1],[2,0,1]], 2))