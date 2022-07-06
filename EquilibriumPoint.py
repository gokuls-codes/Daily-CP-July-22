# User function Template for python3
class Solution:
    # Complete this function
    
    #Function to find equilibrium point in the array.
    def equilibriumPoint(self,A, N):
        # Your code here
        if N == 1:
            return 1

        for i in range(1, N):
            A[i] += A[i-1]

        # print(A)

        for i in range(1, N):
            if A[i-1] == A[-1] - A[i]:
                return i+1

        return -1