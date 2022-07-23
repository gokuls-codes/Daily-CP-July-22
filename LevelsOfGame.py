from typing import List


class Solution:
    def maxLevel(self, h:int,m:int) -> int:
        # code here
        mem = [[None for j in range(1500)] for i in range(1500)]
        
        def dp(h, m):
            
            if h <= 0 or m <= 0:
                return 0
                
            if mem[h][m] is not None:
                return mem[h][m]
                
            v1 = dp(h-2, m-8) + 2
            v2 = dp(h-17, m+7) + 2
            
            mem[h][m] = max(v1, v2)
                
            return mem[h][m]
            
        return dp(h, m) - 1