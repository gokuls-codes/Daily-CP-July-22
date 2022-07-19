class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        n = len(A)
        dct = {i:0 for i in range(1, n+1)}
        
        for ele in A:
            dct[ele] += 1
            
        ans = [-1, -1]
        for key in dct:
            if dct[key] == 2:
                ans[0] = key
            elif dct[key] == 0:
                ans[1] = key
                
        return ans
                