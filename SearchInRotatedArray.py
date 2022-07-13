#User function Template for python3

class Solution:
    def search(self, A : list, l : int, h : int, key : int):
        # l: The starting index
        # h: The ending index, you have to search the key in this range
        # Complete this function
        
        left = l
        right = h
        
        while left <= right:
            mid = (left + right)//2
            
            if A[mid] == key:
                return mid
                
            if A[mid] < A[right]:
                if A[mid] < key <= A[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            
            else:
                if A[mid] > key >= A[left]:
                    right = mid - 1
                else:
                    left = mid + 1
        
        return -1
