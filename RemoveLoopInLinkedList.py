'''
# node class:

class Node:
    def __init__(self,val):
        self.next=None
        self.data=val

'''

class Solution:
    #Function to remove a loop in the linked list.
    def removeLoop(self, head):
        # code here
        # remove the loop without losing any nodes
        visited = set()
        temp = head
        
        while temp!=None:
            visited.add(temp)
            if temp.next in visited:
                temp.next = None
            temp = temp.next
        
        return