# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        if head == None:
            return head
        
        if left == right:
            return head
        
        left_node, right_node = head, head
        stop = False
        
        def helper(right_node, left, right):
            nonlocal left_node, stop
            
            if right == 1:
                return
            
            right_node = right_node.next
            
            if left > 1:
                left_node = left_node.next
                
            helper(right_node, left-1, right-1)
            
            if left_node == right_node or left_node == right_node.next:
                stop = True
                
            if not stop:
                left_node.val, right_node.val = right_node.val, left_node.val
                
                left_node = left_node.next
                
        helper(right_node, left, right)
        
        return head