from typing import List

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:

        n = len(nums)
        ans = [0] * n
        arr = [(nums[i], i) for i in range(n)]

        def merge(arr):
            if len(arr) <= 1:
                return

            length = len(arr)
            mid = length//2

            left = arr[:mid]
            right = arr[mid:]

            merge(left)
            merge(right)

            l1 = mid
            l2 = length - mid

            i, j, k = 0, 0, 0

            count = 0

            while i < l1 and j < l2:
                if left[i] < right[j]:
                    arr[k] = left[i]
                    ind = left[i][1]
                    ans[ind] += count
                    i += 1

                else:
                    count += 1
                    arr[k] = right[j]
                    j += 1

                k += 1

            while i < l1:
                arr[k] = left[i]
                ind = left[i][1]
                ans[ind] += count
                i += 1 
                k += 1

            while j < l2:
                arr[k] = right[j]
                count += 1
                j += 1
                k += 1

        merge(arr)
        
        return ans

print(Solution().countSmaller(nums = [5,2,6,1]))
