class Solution:
            
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numsMapping = { key:value for value, key in enumerate(nums) }
        
        for idx, n in enumerate(nums):
            result = target - n
            if result in numsMapping and numsMapping.get(result)!= idx:
                return [idx, numsMapping.get(result)]


soln = Solution()
print(soln.twoSum([3,2,4],6))
        
        
        