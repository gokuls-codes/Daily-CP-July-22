class Solution:
    def findSwapValues(self,a, n, b, m):
        # Your code goes here
        s1 = sum(a)
        s2 = sum(b)
        
        total = s1 + s2
        if total %2:
            return -1
        
        diff = (s1 - s2)//2
        
        a.sort()
        b.sort()
        
        i, j = 0, 0
        
        while i<n and j<m:
            d = a[i] - b[j]
            if d == diff:
                return 1
                
            if d < diff:
                i += 1
                
            else:
                j += 1
                
        return -1