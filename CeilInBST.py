#Function to return the ceil of given number in BST.

class Solution:
    def findCeil(self,root, inp):
        # code here
        if root == None:
            return -1
        
        if root.key == inp:
            return root.key
            
        elif root.key < inp:
            return self.findCeil(root.right, inp)
            
        v2 = self.findCeil(root.left, inp)
        if v2 >= inp:
            return v2
        else:
            return root.key