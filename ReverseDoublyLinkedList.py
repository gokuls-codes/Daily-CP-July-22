#User function Template for python3

'''
class Node: 
    def __init__(self, data): 
        self.data = data  
        self.next = None
        self.prev = None
'''

def reverseDLL(head):
    #return head after reversing
    temp = None
    cur = head
    while cur:
        temp = cur.prev
        cur.prev, cur.next = cur.next, cur.prev
        cur = cur.prev
        
    if temp:
        return temp.prev
        
    return head