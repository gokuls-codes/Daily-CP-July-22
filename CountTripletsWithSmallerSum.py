class Solution:
    def TripletsWithSmallerSum(self, arr, target):

        arr.sort()
        ans = 0

        for i in range(len(arr) - 2):
            e1 = i+1
            e2 = len(arr) - 1
            
            cur = arr[i] + arr[e1] + arr[e2]

            while e1 < e2:
                cur = arr[i] + arr[e1] + arr[e2]

                if cur >= target:
                    e2 -= 1

                else:
                    ans += (e2-e1)
                    e1 += 1
    
        return ans

print(Solution().TripletsWithSmallerSum([5, 1, 3, 4, 7], 12))