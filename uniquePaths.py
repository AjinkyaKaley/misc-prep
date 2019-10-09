class Solution:
    def uniquePaths(self, m: int, n: int, count:int):
        
        if m < 1 or n < 1:
            return 0

        if m==1 and n==1:
            # print ("1")
            count+=1
            return count

        return self.uniquePaths(m-1,n, count) + self.uniquePaths(m, n-1, count)
        # return

    def uniquePaths2(self, m: int, n: int):
        
        def getPath(m,n,i,j):
            if i == m - 1 and j == n - 1:
                return 1
            
            if 0<= i < m and 0 <= j < n:
                return getPath(m,n,i+1,j) + getPath(m,n,i,j+1)
            return 0
        
        return getPath(m,n,0,0)
    def uniquePathsDP(self, m ,n):
        if m==0 and n==0:
            return 0
        if m==1 and n==1:
            return 1
        result = [[None for i in range(0,n)] for j in range(0,m)]
        result[0][0] = 0
        for i in range(1,m):
            result[i][0] = 1
        for j in range(1,n):
            result[0][j] = 1
        
        for _i in range(1,m):
            for _j in range(1,n):
                result[_i][_j] = result[_i][_j-1] + result[_i-1][_j]
        
        return result[m-1][n-1]
    
                
sln = Solution()
count=0
print(sln.uniquePaths2(3, 2))
