#User function Template for python3


class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def isAnagram(self,a,b):
        #code here
        letters = {chr(x):0 for x in range(97, 123)}
        
        for ch in a:
            letters[ch] += 1
            
        for ch in b:
            letters[ch] -= 1
            
        for key in letters.keys():
            if letters[key] != 0:
                return False
                
        return True