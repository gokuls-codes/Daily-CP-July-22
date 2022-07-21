from typing import List, Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        
        def merge2lists(list1, list2):
            temp1 = list1
            temp2 = list2
            
            res = ListNode()
            temp = res
            
            while temp1 and temp2:
                if temp1.val < temp2.val:
                    temp.next = ListNode(temp1.val)
                    temp = temp.next
                    temp1 = temp1.next
                else:
                    temp.next = ListNode(temp2.val)
                    temp = temp.next
                    temp2 = temp2.next
                    
            while temp1:
                temp.next = ListNode(temp1.val)
                temp = temp.next
                temp1 = temp1.next
                
            while temp2:
                temp.next = ListNode(temp2.val)
                temp = temp.next
                temp2 = temp2.next
                
            return res.next
        
        arr1 = lists[0]
        
        for i in range(1, len(lists)):
            arr1 = merge2lists(arr1, lists[i])
            
        return arr1