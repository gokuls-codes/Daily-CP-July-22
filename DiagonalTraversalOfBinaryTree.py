#User function Template for python3

'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
#Complete the function below
class Solution:
    def diagonal(self,root):
        #:param root: root of the given tree.
        #return: print out the diagonal traversal,  no need to print new line
        #code here
        from collections import deque

        ans = []
        temp = root

        lq = deque()

        while temp!=None:
            ans.append(temp.data)

            if temp.left != None:
                lq.appendleft(temp.left)
            
            if temp.right != None:
                temp = temp.right

            else:
                if len(lq) >= 1:
                    temp = lq.pop()
                else:
                    temp = None

        return ans