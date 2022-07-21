#User function Template for python3

#Function to push all the elements into the stack.
def _push(a,n):
    if n == 0:
        return []
    
    # code here
    stack = []
    min_till_now = a[0]
    
    for i in range(n):
        if a[i] < min_till_now:
            min_till_now = a[i]
        stack.append((a[i], min_till_now))
        
    return stack
        
#Function to print minimum value in stack each time while popping.    
def _getMinAtPop(stack):
    while stack != []:
        ele = stack.pop()
        print(ele[1], end = " ")
    
    return