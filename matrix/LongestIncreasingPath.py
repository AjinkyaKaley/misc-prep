class Solution:

    def longestIncreasingPathInGrid(self, grid):
        m = len(grid)
        n = len(grid[0])
        visited = [[False for i in range(n)] for j in range(m)]
        ans = float("-inf")
        cache = [[0 for i in range(n)] for j in range(m)]

        def dfs(i, j, prev, visited):

            if i < 0 or j < 0 or i >= m or j >= n or visited[i][j] or grid[i][j] <= prev:
                return 0
            
            if cache[i][j] != 0:
                return cache[i][j]
            
            cache[i][j] = 1+ max(
                dfs(i + 1, j, grid[i][j], visited),
                dfs(i, j + 1, grid[i][j], visited),
                dfs(i - 1, j, grid[i][j], visited),
                dfs(i, j - 1, grid[i][j], visited)
            )
            
            return cache[i][j]

        for i in range(m):
            for j in range(n):
                if grid[i][j] not in visited:
                    ans = max(ans, dfs(i, j, float("-inf"),visited))
        
        print(ans)

sln = Solution()
sln.longestIncreasingPathInGrid(
    [
        [9, 9, 4],
        [6, 6, 8],
        [2, 1, 1]
    ]
)

