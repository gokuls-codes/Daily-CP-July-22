from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        if matrix[0][0] == target:
            return True
        
        def bst(arr, target):
            left = 0
            right = len(arr) - 1

            while left <= right:
                mid = (left + right)//2
                if target == arr[mid]:
                    return mid, True

                elif target < arr[mid]:
                    right = mid - 1

                else:
                    left = mid + 1

            return left, False

        arr = [matrix[i][0] for i in range(len(matrix))]
        val = False
        if len(arr) > 1:
            row_no, val = bst(arr, target)
        else:
            row_no = 0

        if not val:
            row_no = row_no - 1

        if len(matrix[0]) > 1:
            col_no, val = bst(matrix[row_no], target)
        else:
            col_no = 0
        
        if val:
            return True

        return False

soln = Solution()
print(soln.searchMatrix(matrix = [[1]], target = 1))