#User function Template for python3

def reaching_height (n, arr) : 
    #Complete the function
    arr.sort(reverse=True)
    
    ans = [0 for _ in range(n)]
    ans[0] = arr[0]
    for i in range(1, n//2 + 1):
        if 2*i < n:
            ans[2*i] = arr[i]
        ans[2*i - 1] = arr[-i]

    sub = 1
    res = 0
    for i in range(n):
        res += sub * ans[i]
        sub = sub * -1
        if res == 0:
            return [-1]

    return ans