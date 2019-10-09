class Solution:

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def helper(n, visited):
            if n == 1:
                return True
            if n in visited:
                return False
            visited.add(n)
            new_n = 0
            while n > 0:
                t = n % 10
                new_n += t*t
                n = n//10
            return helper(new_n, visited)
        return helper(n, set())
sln = Solution()
sln.isHappy(19)

