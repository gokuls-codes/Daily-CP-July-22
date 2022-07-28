# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return root
        
        temp = root.right
        root.right = self.flatten(root.left)
        t2 = root
        while t2.right is not None:
            t2.left = None
            t2 = t2.right
            
        t2.right = self.flatten(temp)
        
        while t2.right is not None:
            t2.left = None
            t2 = t2.right
        
        return root
        