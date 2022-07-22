# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head == None:
            return head
        
        t1 = temp1 = ListNode(0)
        t2 = temp2 = ListNode(0)
        
        temp = head
        
        while temp:
            if temp.val < x:
                t1.next = temp
                t1 = t1.next
            else:
                t2.next = temp
                t2 = t2.next
            
            temp = temp.next
        
        t2.next = None
        t1.next = temp2.next
        
        return temp1.next
                