class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        self.totalIslands = 0
        self.visited = [[False]*len(grid[0])]*len(grid)

        def helper(i, j, grid):
            if i < 0 or j < 0 or i > len(grid) or j > len(grid[0]):
                return False

            if not self.visited[i][j] and grid[i][j] == 1:
                self.visited[i][j] = True
                helper(i, j+1, grid)
                helper(i, j-1, grid)
                helper(i+1, j, grid)
                helper(i-1, j, grid)
            else:
                return False

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not self.visited[i][j] and grid[i][j] == 1:
                    helper(i, j, grid)
                    self.totalIslands += 1

        return self.totalIslands
sln = Solution()
grid = [[1, 1, 1, 1, 0], [1, 1, 0, 1, 0], [1, 1, 0, 0, 0], [0, 0, 0, 0, 0]]
print(sln.numIslands(grid))
