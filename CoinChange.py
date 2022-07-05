class Solution:
    def count(self, S, m, n): 
        # code here 
        mem = [0 for _ in range(n+1)]
        
        mem[0] = 1
        
        for i in range(m):
            for j in range(S[i], n+1):
                mem[j] += mem[j-S[i]]
                
        return mem[n]