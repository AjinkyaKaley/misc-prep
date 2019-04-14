class Solution:
    def recPermute(self, result, current, nums):
        if len(nums) == 2 :
            result.append(current+[nums[0],nums[1]])
            result.append(current+[nums[1],nums[0]])
            return
        for i in range(len(nums)):
            self.recPermute(result, current+ [nums[i]], nums[:i]+nums[i+1:])

    def permute(self, nums):
        if len(nums) == 0: return [] 
        if len(nums) == 1 : return [[nums[0]]]

        result=[]
        current=[] 
        self.recPermute(result,current,nums)
        return result

sln = Solution()
print(sln.permute([1,1,2]))