#User function Template for python3

class Solution:
    def longestCommonPrefix(self, arr, n):
        # code here
        prefix = arr[0]
        for word in arr:
            if word.startswith(prefix):
                continue
            
            while len(prefix) > 0 and not word.startswith(prefix):
                prefix = prefix[:-1]
                
            if len(prefix) == 0:
                return -1
        # print(prefix)
                
        return prefix