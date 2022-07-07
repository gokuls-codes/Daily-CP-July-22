class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        if (len(s1) + len(s2)) != len(s3):
            return False
        
        mem = [[-1 for _ in range(len(s2))] for _ in range(len(s1))]
        
        def helper(i, j, k):
            if i >= len(s1):
                return (s2[j:] == s3[k:])
            if j >= len(s2):
                return (s1[i:] == s3[k:])
            
            if mem[i][j] >= 0:
                return mem[i][j] == 1
            
            ans = False
            if (s3[k] == s1[i] and helper(i+1, j, k+1)) or (s3[k] == s2[j] and helper(i, j+1, k+1)):
                ans = True
                
            mem[i][j] = int(ans)
            return ans
        
        return helper(0, 0, 0)
        


soln = Solution()
print(soln.isInterleave("aabaac",
"aadaaeaaf",
"aadaaeaabaafaac"))