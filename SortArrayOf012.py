class Solution:
    def sort012(self,arr,n):
        # code here
        counter = {i:0 for i in range(3)}
        
        for num in arr:
            counter[num] += 1
            
        i = 0
        while i < counter[0]:
            arr[i] = 0
            i += 1
        while i < counter[0] + counter[1]:
            arr[i] = 1
            i += 1
        while i < len(arr):
            arr[i] = 2
            i += 1