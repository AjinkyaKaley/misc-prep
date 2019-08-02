class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArr(self, A):
        self.maxAbsDiff = float("-inf")
        return self.helper(A,[],0)
        
    def helper(self,nums,subset,idx):
        if len(subset) == 2:
            print(subset)
            return
        
        for i in range(idx,len(nums)):
            subset.append(nums[i])
            self.helper(nums,subset,i+1)
            subset.pop()
        
sln = Solution()
sln.maxArr([1, 3, -1])