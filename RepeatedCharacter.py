
class Solution:
    def firstRep(self, s):
        # code here
        counter = {}
        for char in s:
            if char in counter:
                counter[char] += 1
            else:
                counter[char] = 1
                
        for char in s:
            if counter[char] > 1:
                return char
                
        return -1