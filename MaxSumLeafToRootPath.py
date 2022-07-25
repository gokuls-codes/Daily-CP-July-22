#User function Template for python3

class Solution:
    def maxPathSum(self, root):
        #code here
        
        def helper(root):
            if root == None:
                return 0
            
            elif root.right == None and root.left == None:
                return root.data
            
            else:
                return root.data + max(helper(root.right), helper(root.left))
                
        return helper(root)
