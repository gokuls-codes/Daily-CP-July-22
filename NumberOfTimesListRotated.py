class Solution:
    def NumberOfTimesRotated(self, arr):
        right = len(arr) - 1
        left = 0

        while left <= right:
            mid = (left + right) // 2

            if arr[mid] < arr[mid-1]:
                return mid

            if arr[mid] < arr[right]:
                right = mid - 1

            else:
                left = mid + 1

        return 0

print(Solution().NumberOfTimesRotated([ 1, 2, 3, 4 ,5, 8, 9]))