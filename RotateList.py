# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        new_head = ListNode()
        temp = head
        n = 0
        while temp.next!=None:
            n += 1
            temp = temp.next

        k = k % (n + 1)
        if k == 0:
            return head
        
        temp = head
        i = 0

        while i < (n-k):
            temp = temp.next
            i+=1

        new_head = temp.next
        temp.next = None
        
        temp = new_head
        while temp.next!= None:
            temp = temp.next
        temp.next = head

        return new_head
        