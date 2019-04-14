class Solution:
    def numTrees(self, n: int, result) -> int:
        if n<=1:
            return 1
        else:
            total = 0
            for i in range(1,n+1):
                if result[i-1] is None:
                    result[i-1] = self.numTrees(i-1, result)
                if result[n-i] is None:        ## Left subtree
                    result[n-i] = self.numTrees(n-i, result)      ## Right subtree
                total += result[i-1] * result[n-i]              ## left and right subtree can be combined to form a subtree

        return total

sln = Solution()
n = 3
result = [ None for i in range(1,n+1)]
print(sln.numTrees(n,result))