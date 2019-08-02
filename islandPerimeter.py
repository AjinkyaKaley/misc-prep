class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.visited = [[-1 for i in range(len(grid[0]))] for j in range(len(grid))]
        self.perimeter = 0
        def helper(i,j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                return
            
            if self.visited[i][j] == 1:
                self.perimeter -= 2
                return

            if self.visited[i][j] == -1 and grid[i][j] == 1:
                self.visited[i][j] = 1
                self.perimeter+=4
                helper(i + 1, j)
                helper(i - 1, j)
                helper(i, j + 1)
                helper(i, j - 1)
                self.visited[i][j] = 2
            
            return
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return helper(i, j)

    # def islandPerimeter(self, grid):
    #     m, n = len(grid), len(grid[0])
    #     visited = [[-1 for i in range(n)] for j in range(m)]    # -1: unvisited
    #     self.res = 0

    #     def dfs(i, j):
    #         outOfRange = i < 0 or i >= m or j < 0 or j >= n
    #         if outOfRange or visited[i][j] == 2 or grid[i][j] == 0:
    #             return
    #         if visited[i][j] == 1:   # 1: meet the island on the path of visiting
    #             # if 2 edges are connected with each other, we need to get rid of the overlaping edges (total_edges = 4 + 4 - 2)
    #             self.res -= 2
    #             return
    #         self.res += 4    # one cell has 4 edges
    #         visited[i][j] = 1    # mark it as visiting
    #         for a, b in [[0, -1], [-1, 0], [0, 1], [1, 0]]:
    #             dfs(i + a, j + b)
    #         visited[i][j] = 2         # 2: visited
    #         return

    #     for i in range(m):
    #         for j in range(n):
    #             dfs(i, j)
    #     return self.res

sln = Solution()
data = [[0, 1, 0, 0],
        [1, 1, 1, 0],
        [0, 1, 0, 0],
        [1, 1, 0, 0]]
sln.islandPerimeter(data)
