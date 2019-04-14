class Solution:
    def minPathSum(self, grid):
        
        rows = len(grid)
        columns = len(grid[0])
        if rows == 0 or columns == 0:
            return 0
            
        for _i in range(1, rows):
            grid[_i][0] = grid[_i-1][0] + grid[_i][0]

        for _j in range(1, columns):
            grid[0][_j] = grid[0][_j-1] + grid[0][_j]

        for i in range(1,rows):
            for j in range(1, columns):
                grid[i][j] = grid[i][j] + min(grid[i-1][j], grid[i][j-1])
        
        return grid[rows-1][columns-1]

sln = Solution()
print(sln.minPathSum([
  []
#   [1,5,1]
#   [4,2,1]
]))
