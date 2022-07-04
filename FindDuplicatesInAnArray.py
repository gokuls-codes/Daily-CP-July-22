class Solution:
    def duplicates(self, arr, n): 
    	# code here
    	counter = {i:0 for i in range(len(arr))}
    	
    	for num in arr:
    	    counter[num] += 1
    	
    	ans = []
    	
    	for key in counter:
    	    if counter[key] > 1:
    	        ans.append(key)
    	        
        if ans == []:
            return [-1]
        
        return ans