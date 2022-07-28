#User function Template for python3

class Solution:
    def knots(self, M, N, K):
        # code here
        if K > M or K > N:
            return 0
            
        mem = [1, 1]
            
        def find_factorial(n):
            i = len(mem)
            if n < i:
                return mem[n]
            
            while i <= n:
                mem.append(mem[-1] * i)
                i += 1
            
            return mem[n]
            
        c1 = find_factorial(M) // (find_factorial(M-K) * find_factorial(K))
        c2 = find_factorial(N) // (find_factorial(N-K) * find_factorial(K))

        return (c1 * c2)%1000000007