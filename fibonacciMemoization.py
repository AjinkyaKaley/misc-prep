class Solution:
    def fib(self,n, lookup):
        # Base case
        if n == 0 or n == 1:
            lookup[n] = n

        # If the value is not calculated previously then calculate it
        if lookup[n] is None:
            lookup[n] = self.fib(n-1, lookup) + self.fib(n-2, lookup)

        # return the value corresponding to that value of n
        return lookup[n]

sln = Solution()
sln.fib(5,[None]*100)