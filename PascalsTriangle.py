from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        mem = [[1], [1,1]]
        
        def helper(n):
            print(n)

            if n <= len(mem):
                return
            
            if n - 1 > len(mem):
                helper(n-1)
                
            cur = [1]
            # print(mem)
            for i in range(len(mem[n-2]) - 1):
                cur.append(mem[n-2][i] + mem[n-2][i+1])
            
            cur.append(1)
            mem.append(cur)
        
        helper(numRows)
        
        return mem[:numRows]
            
print(Solution().generate(numRows = 5))