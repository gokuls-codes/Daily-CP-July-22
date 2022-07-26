#User function Template for python3


class Solution:
    
    #Function to find the smallest window in the string s consisting
    #of all the characters of string p.
    def smallestWindow(self, s, p):
        #code here
        
        n = len(s)
        if n < len(p):
            return "-1"

        from collections import Counter
        
        left = 0
        min_length = 10**5
        
        counter = Counter(list(p))
        count = len(counter)
        
        i, j = 0, 0
        
        while j < n:
            counter[s[j]] -= 1
            if counter[s[j]] == 0:
                count -= 1
                
                while count == 0:
                    if min_length > j -i + 1:
                        min_length = j - i + 1
                        left = i
                        
                    counter[s[i]] += 1
                    if counter[s[i]] > 0:
                        count += 1
                    
                    i += 1
                    
            j += 1
            
        if min_length > n:
            return "-1"
            
        return s[left:left+min_length]

print(Solution().smallestWindow("zoomlazapzo", "oza"))