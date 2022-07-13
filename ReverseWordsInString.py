
# User function Template for python3

class Solution:
    
    #Function to reverse words in a given string.
    def reverseWords(self,S):
        # code here 
        lst = S.split('.')
        lst.reverse()
        
        return '.'.join(lst)