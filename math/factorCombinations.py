class Solution:
    def getFactors(self, n: int):

        self.solution = []
        if n == 1:
            return []

        def helper(idx, curr_factors, _n, n):
            # if _n > n:
            #     return

            if n <= 1:
                self.solution += [curr_factors]
                return

            for num in range(idx, n+1):
                if n % num == 0:
                    helper(num, curr_factors+[num], _n * num, n//num)

        helper(2, [], 1, n)
        return self.solution

sln = Solution()
sln.getFactors(18)