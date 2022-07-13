#User function Template for python3

class Solution:
    
    #Function to find the minimum indexed character.
    def minIndexChar(self,Str, pat): 
        #code here
        st = set(list(pat))
        
        for i in range(len(Str)):
            if Str[i] in st:
                return i
            
        return -1