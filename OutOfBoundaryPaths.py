class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        
        mem = [[[-1 for _ in range(maxMove+1)] for _ in range(n)] for _ in range(m)]

        def helper(m, n, N, i, j):
            if i>=m or j >=n or i < 0 or j < 0:
                return 1
            if N == 0:
                return 0
            if mem[i][j][N] != -1:
                return mem[i][j][N]

            mem[i][j][N] = helper(m,n,N-1,i-1,j) + helper(m,n,N-1,i+1,j) + helper(m,n,N-1,i,j-1) + helper(m,n,N-1,i,j+1)

            return mem[i][j][N]

        return helper(m,n,maxMove, startRow, startColumn) % 1000000007

# soln = Solution()
# print(soln.findPaths(m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1))