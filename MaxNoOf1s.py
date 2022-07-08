#User function Template for python3

class Solution:
    def maxOnes (self, Mat, N, M):
        # code here 
        ans = -1
        zero_count = M
        
        for i in range(N):
            low, high = 0, M - 1
            while low<=high:
                mid = low + (high-low)//2
                if Mat[i][mid] == 0:
                    low = mid+1
                else:
                    high = mid-1
            if zero_count > low:
                zero_count = low
                ans = i
                
        return ans