
class Solution:
    def countDistinct(self, A, N, K):
        # Code here
        from collections import defaultdict
        
        ans = []
        seen = defaultdict(lambda:0)
        distinct = 0
        
        for i in range(K):
            if seen[A[i]] == 0:
                distinct += 1
            seen[A[i]] += 1
                
        ans.append(distinct)
        
        for i in range(1, N-K+1):
            if seen[arr[i-1]] == 1:
                distinct -= 1
            seen[arr[i-1]] -= 1
            
            if seen[arr[i+K-1]] == 0:
                distinct += 1
                
            seen[arr[i+K-1]] += 1
            
            ans.append(distinct)
            
        return ans