class Solution:
    def myPow(self, x, o, n):
        if n == 1:
            return x

        return self.myPow(x*o, o,n-1)

sln = Solution()
print(sln.myPow(3,3,3))

