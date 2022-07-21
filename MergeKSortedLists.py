# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        
        t = []
        curr = []
        length = 0

        for lst in lists:
            t.append(lst)
            if lst is not None:
                curr.append(lst.val)
                length += 1
            else:
                curr.append(None)

        res = ListNode()
        temp = res

        # print(length)

        while length > 0:
            minimum = min(x for x in curr if x is not None)
            ind = curr.index(minimum)

            temp.next = ListNode(minimum)
            temp = temp.next

            t[ind] = t[ind].next

            if t[ind]:
                curr[ind] = t[ind].val
            else:
                curr[ind] = None
                length -= 1

        return res.next