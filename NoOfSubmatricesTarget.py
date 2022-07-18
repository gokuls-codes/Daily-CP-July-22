from typing import List

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m = len(matrix[0])
        n = len(matrix)

        ans = 0

        for row in matrix:
            for j in range(1, m):
                row[j] = row[j] + row[j-1]

        # print(matrix)

        for j in range(m):
            for k in range(j, m):
                res = {0: 1}
                cur = 0

                for row in matrix:
                    cur += row[k] - (row[j-1] if j > 0 else 0)
                    if cur - target in res: 
                        ans += res[cur-target]
                    
                    if cur in res:
                        res[cur] += 1
                    else:
                        res[cur] = 1

        return ans


print(Solution().numSubmatrixSumTarget(matrix = [[1,-1],[-1,1]], target = 0))