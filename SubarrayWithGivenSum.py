#Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self,arr, n, s):
       #Write your code here
        left = 0
        right = 1
        current_sum = arr[0]

        while right <= n:
            while current_sum > s and left < right -1:
                current_sum -= arr[left]
                left += 1
            
            if current_sum == s:
                return [left+1, right]

            if right < n:
                current_sum += arr[right]

            right += 1

        return [-1]