class Solution:

    def getPermutation(self, n, k):
        factorial = []
        factorial.append(1)
        _sum = 1
        nums = []
        for i in range(1, n + 1):
            _sum *= i
            factorial.append(_sum)
            nums.append(i)
        
        k -= 1
        res=""
        for i in range(1,n+1):
            rootIdx = k // factorial[n - i]
            res += str(nums[rootIdx])
            nums = nums[:rootIdx] + nums[rootIdx + 1:]
            k = k - (rootIdx * factorial[n - i])

        return res

sln = Solution()
sln.getPermutation(4,1)