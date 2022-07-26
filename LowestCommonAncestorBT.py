# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = None
        def helper(curr):
            nonlocal ans
            if curr == None:
                return False
            
            left = helper(curr.left)
            right = helper(curr.right)
            
            middle = (curr == p) or (curr == q)
            
            if middle + left + right >= 2:
                ans = curr
                
            return middle or left or right
        
        helper(root)
        
        return ans
        
                