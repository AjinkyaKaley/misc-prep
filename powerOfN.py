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
print(sln.myPow(2, -3))

