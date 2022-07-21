class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class ListNode:
    def __init__ (self, val =0, next = None):
        self.val = val
        self.next = next

class Solution:

    def flattenBST(self, root):
        
        ans = ListNode()
        temp = ans
        # arr = []

        def inorder(root):
            nonlocal temp

            if root == None:
                return

            inorder(root.left)
            temp.next = ListNode(root.val)
            # arr.append(temp.val)
            temp = temp.next
            inorder(root.right)

        inorder(root)
        # print(arr)
        return ans.next

root = Node(5)
root.left = Node(3)
root.right = Node(7)
root.left.left = Node(2)
root.left.right = Node(4)
root.right.left = Node(6)
root.right.right = Node(8)

print((Solution().flattenBST(root)).val)