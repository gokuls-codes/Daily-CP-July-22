# your task is to complete this function
# function should return an integer
'''
class node:
    def __init__(self):
        self.data = None
        self.next = Non
'''
class Solution:
    def maxPalindrome(self,head):
        # Code here
        
        res = 0
        prev = None
        cur = head
        
        def helper(n1, n2):
            count = 0
            while n1!=None and n2!=None:
                if n1.data == n2.data:
                    count += 1
                else:
                    break
                
                n1 = n1.next
                n2 = n2.next
            
            return count
        
        while cur!=None:
            next = cur.next
            cur.next = prev
            
            res = max(res, 2*helper(prev, next) + 1)
            
            res = max(res, 2*helper(cur, next))
            
            prev = cur
            cur = next
            
        return res