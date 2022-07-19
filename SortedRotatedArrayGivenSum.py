class Solution:
    def SortedRotateGivenSum(self, arr, target):

        maxval = arr[0]
        max_ind = 0

        length = len(arr)

        for i in range(length):
            if arr[i] > maxval:
                maxval = arr[i]
                max_ind = i

        if max_ind == length-1:
            min_ind = 0
        else:
            min_ind = max_ind + 1

        while arr[min_ind] < arr[max_ind]:
            if arr[min_ind] + arr[max_ind] == target:
                return True

            if arr[min_ind] + arr[max_ind] > target:
                if max_ind == 0:
                    max_ind = length - 1

                else:
                    max_ind -= 1

            else:
                if min_ind == length-1:
                    min_ind = 0

                else:
                    min_ind += 1

        return False

print(Solution().SortedRotateGivenSum([11, 15, 26, 38, 9, 10], 45))