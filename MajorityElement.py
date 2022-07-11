#User function template for Python 3

class Solution:
    def majorityElement(self, A, N):
        #Your code here
        from collections import Counter
        counter = Counter(A)
        
        for key in counter:
            if counter[key] > N/2:
                return key
        
        return -1