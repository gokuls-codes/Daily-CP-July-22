
class Solution:
    def MissingNumber(self,array,n):
        # code here
        array.append(0)
        array.append(0)
        for i in range(n):
            r = array[i]%(n+1)
            array[r] += (n+1)
        
        print(array)

        for i in range(n+1):
            if array[i]/(n+1) < 1:
                return i

soln = Solution()
print(soln.MissingNumber([6, 1, 2, 8, 3, 4, 7, 10, 5], 10))