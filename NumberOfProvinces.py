#User function Template for python3

class Solution:
    def numProvinces(self, adj, V):
        # code here 
        
        visited = set()
        
        def dfs(v):
            for i in range(len(adj[v])):
                if adj[v][i] == 1 and i not in visited:
                    visited.add(i)
                    dfs(i)
                    
        res = 0
        for i in range(V):
            if i not in visited:
                dfs(i)
                res += 1
                
        return res
