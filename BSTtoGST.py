#User function Template for python3

'''
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
        
'''

class Solution:
    def transformTree(self, root):
        #code here
        mem = {}
        inorder = []
        
        def inorderTraversal(root):
            if root == None:
                return
            
            inorderTraversal(root.right)
            mem[root.data] = 0
            inorder.append(root.data)
            inorderTraversal(root.left)
        
        def change(root):
            if root == None:
                return
            root.data = mem[root.data]
            change(root.left)
            change(root.right)
        
        inorderTraversal(root)
        
        for i in range(1, len(inorder)):
            mem[inorder[i]] = inorder[i-1] + mem[inorder[i-1]]
            
        change(root)
        
        return root