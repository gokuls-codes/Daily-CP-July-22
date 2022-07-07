
class Solution:
    #Back-end complete function Template for Python 3
    
    #Function to find the leaders in the array.
    def leaders(self, A, N):
        #Code here
        right_max = A[-1]
        no_leaders = [A[-1]]
        
        for i in range(N-2, -1, -1):
            if A[i] >= right_max:
                no_leaders.append(A[i])
                right_max = A[i]
                
        no_leaders.reverse()
        return no_leaders