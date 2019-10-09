class Solution:
    def myPow(self, x, n):
        if n == 0:
            return 1
        temp = self.myPow(x, int(n/2))
        if n % 2 == 0:
            return temp*temp
        else:
            if n > 0:
                return temp*temp*x
            else:
                return (temp * temp) / x
                
    # Python3 code for extended version
# of power function that can work
# for float x and negative y


    def myPow2(self, x: float, n: int) -> float:

        def helper(x, n):
            if n == 0:
                return 1.0

            s = helper(x, n//2)
            if n % 2 == 0:
                return s*s
            else:
                return s * s * x

        if n < 0:
            n = -n
            x = 1/x
        return helper(x, n)

    def power(self,x, y):

        if(y == 0):
            return 1
        temp = self.power(x, int(y / 2))

        if (y % 2 == 0):
            return temp * temp
        else:
            if(y > 0):
                return x * temp * temp
            else:
                return (temp * temp) / x


# Driver Code


# This code is contributed by Smitha Dinesh Semwal.


sln = Solution()
print(sln.myPow2(2.00000,
                10))

