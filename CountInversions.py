class Solution:
    #User function Template for python3
    
    # arr[]: Input Array
    # N : Size of the Array arr[]
    #Function to count inversions in the array.
    def inversionCount(self, arr, n):

        ans = [0 for _ in range(n)]
        # Your Code Here
        
        def merge(arr):
            if len(arr) <= 1:
                return

            length = len(arr)
            mid = length//2

            left = arr[:mid]
            right = arr[mid:]

            merge(left)
            merge(right)

            i, j, k = 0, 0, 0
            l1 = mid
            l2 = length - mid

            count = 0

            while i < l1 and j < l2:
                if left[i] < right[j]:
                    index = left[i][1]
                    arr[k] = left[i]
                    ans[index] += count
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                    count += 1

                k += 1

            while i < l1:
                index = left[i][1]
                arr[k] = left[i]
                ans[index] += count
                i += 1
                k += 1

            while j < l2:
                arr[k] = right[j]
                count += 1
                k += 1
                j += 1

        a = [(arr[i], i) for i in range(n)]
        merge(a)

        return sum(ans)


print(Solution().inversionCount([2, 3, 4, 5, 6], 5))