class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        ##Your code here
        current = arr[0]
        maxsum = current
        
        for i in range(1, N):
            current = max(arr[i], current + arr[i])
            
            maxsum = max(maxsum, current)
        
        return maxsum     