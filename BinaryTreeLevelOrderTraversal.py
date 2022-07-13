# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        
        def helper(node, depth):
            if node == None:
                return
            
            if depth >= len(ans):
                ans.append([])
            
            ans[depth].append(node.val)
            
            helper(node.left, depth+1)
            
            helper(node.right, depth+1)
            
        helper(root, 0)
        
        return ans


# DFS, similar to Binary tree right side view problem