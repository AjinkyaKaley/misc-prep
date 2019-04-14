class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[0][0]==1:
            return 0
        if m==0 and n ==0 :
            return 0
        
        if m ==1 and n==1 and obstacleGrid[m-1][n-1] != 1:
            return 1
        elif m==1 and n==1 and obstacleGrid[m-1][n-1] == 0:
            return 0

        result = [[None for i in range(0,n)] for j in range(0,m)]
        
        result[0][0] = 0
        for i in range(0,m):
            for j in range(0,n):
                if obstacleGrid[i][j] == 1:
                    result[i][j] = 0
        
        for i in range(1,m):
            if obstacleGrid[i][0] != 1 and result[i-1][0] != 0 and i-1 > 0:
                result[i][0] = 1
            else:
                result[i][0] = 0
        
        for j in range(1,n):
            if obstacleGrid[0][j] != 1 and result[0][j-1] != 0 and j-1 !=0:
                result[0][j] = 1
            else:
                result[0][j] = 0
        
        for _i in range(1,m):
            for _j in range(1,n):

                if result[_i][_j] != 0:
                    result[_i][_j] = result[_i][_j-1] + result[_i-1][_j]
        
        return result[m-1][n-1]

sln = Solution()
print(sln.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))