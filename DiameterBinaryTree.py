
class Solution:
    
    #Function to return the diameter of a Binary Tree.
    def diameter(self,root):
        # Code here
        if root is None:
            return 0
        diameter = 0
        def helper(node):
            nonlocal diameter
            if node is None:
                return 0
            
            left = helper(node.left)
            right = helper(node.right)
            
            if left + right + 1> diameter:
                diameter = left + right + 1
                
            return max(left, right) + 1
            
        helper(root)
        return diameter
