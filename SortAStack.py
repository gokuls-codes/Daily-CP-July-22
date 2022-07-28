class Solution:
    # your task is to complete this function
    # function sort the stack such that top element is max
    # funciton should return nothing
    # s is a stack
    def sorted(self, s):
        # Code here
        arr = []
        while len(s) != 0:
            arr.append(s.pop())
        
        # print(arr)
        arr.sort()
        
        for ele in arr:
            s.append(ele)
            
        return s