class Solution:
    def combinationSum(self, nums, target):
        
        def helper(nums, target, curr_sum, combinations, startIdx):

            if curr_sum == target:
                print(combinations)

            if len(combinations) == len(nums):
                return
                
            for i in range(startIdx, len(nums)):
                combinations += [nums[i]]
                helper(nums, target, curr_sum + nums[i], combinations,i)
                combinations.pop()

        helper(nums, target, 0, [],0)
        
sln = Solution()
print(sln.combinationSum([2, 3, 6, 7], 7))

