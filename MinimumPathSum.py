class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        mem = {}

        mem[(0,0)] = grid[0][0]

        for i in range(1, len(grid)):
            mem[(i, 0)] = mem[(i-1, 0)] + grid[i][0]

        for i in range(1, len(grid[0])):
            mem[(0, i)] = mem[(0, i-1)] + grid[0][i]

        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                mem[(i,j)] = grid[i][j] + min(mem[(i-1, j)], mem[(i, j-1)])

        return mem[(len(grid)-1, len(grid[0]) - 1)]