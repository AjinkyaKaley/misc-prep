class Solution:

    def maxProductSubarray(self, nums):

        r = nums[0]
        imax = r
        imin = r
        for i in range(1,len(nums)):

            if nums[i] < 0:
                imax, imin = imin, imax
                
            imax = max(nums[i], nums[i] * imax)
            imin = min(nums[i], nums[i] * imin)
            r = max(imax, r)
            
sln = Solution()
print(sln.maxProductSubarray([2, -3, -2, 4]))
