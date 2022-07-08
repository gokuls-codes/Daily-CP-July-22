#User function Template for python3

class Solution:
    def allPairs(self, A, B, N, M, X):
        # Your code goes here
        A.sort()
        B.sort(reverse=True)
        
        ans = []
        
        i, j = 0, 0
        while i < N and j < M:
            if A[i] + B[j] == X:
                ans.append([A[i], B[j]])
                i += 1
                j += 1
            
            elif A[i] + B[j] > X:
                j += 1
            else:
                i += 1
                
        
        return ans