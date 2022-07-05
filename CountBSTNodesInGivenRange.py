#Function to count number of nodes in BST that lie in the given range.
class Solution:
    def getCount(self,root,low,high):
        ##Your code here
        if root == None:
            return 0
        if low <= root.data <= high:
            return 1 + self.getCount(root.left, low, high) + self.getCount(root.right, low, high)
        if low > root.data:
            return self.getCount(root.right, low, high)
        if high < root.data:
            return self.getCount(root.left, low, high)
        
