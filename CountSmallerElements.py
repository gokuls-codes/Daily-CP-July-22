#User function Template for python3
class Solution:

	def constructLowerArray(self,arr, n):
		# code here
		
		def merge(arr):
		    
		    if len(arr) <= 1:
		        return
		    
		    n = len(arr)
		    mid = n//2
		    left = arr[:mid]
		    right = arr[mid:]
		    
		    merge(left)
		    merge(right)
		    
		    i,j,k = 0, 0, 0
		    l1 = mid
		    l2 = n - mid
		    
		    count = 0
		    while i < l1 and j < l2:
		        if left[i][0] > right[j][0]:
		            arr[k] = right[j]
		            j += 1
		            count += 1
		        else:
		            index = left[i][1]
		            arr[k] = left[i]
		            ans[index] += count
		            i += 1
		        k += 1
		        
		    while i < l1:
		        index = left[i][1]
		        arr[k] = left[i]
		        ans[index] += count
		        i += 1
		        k += 1
		       
		    while j < l2:
		        arr[k] = right[j]
		        j += 1
		        count += 1
		        k += 1
		        
	    a = [(arr[i], i) for i in range(n)]
	    ans = [0 for _ in range(n)]
	    merge(a)
	    
	    return ans
		            
