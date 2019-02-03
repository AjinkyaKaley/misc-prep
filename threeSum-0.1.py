class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    sum = nums[i] + nums[j] + nums[k]
                    if sum == 0:
                        arr = [nums[i], nums[j], nums[k]]
                        results.append(arr)

        return results

sln = Solution()
print(sln.threeSum([-1,0,1,2,-1,4]))
#-1,-1,0,1,2,4