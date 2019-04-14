class Solution:

    def combinationSum(self, candidates, target):
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        return res
    
    def dfs(self, nums, target, index, path, res):
        if target < 0:
            return  # backtracking
        if target == 0:
            res.append(path)
            return 
        for i in range(index, len(nums)):
            self.dfs(nums, target-nums[i], i, path+[nums[i]], res)

    def combinationSum(self, candidates, target):
        candidates.sort()
        return self._combinationSum(candidates, target, [])
        
        
    def _combinationSum(self, candidates, target, item):
        if not candidates:
            return []
        
        c = candidates[0]
        if c > target:
            return []
        if c == target:
            return [item+[c]]
        
        return self._combinationSum(candidates[1:], target, item)+self._combinationSum(candidates, target-c, item+[c])

        # def helper(self, candidates, target, total):

        #     if total == target:
        #         return True
        #     root=candidates[0]
        #     summation = root+ total
        #     if summation <= target:
        #         ret = self.helper(candidates[1:], target, summation)
        #         if ret:
        #             print(total)
        #             return True
        #     elif summation > target:
        #         return False
        #     while summation <= target:
        #         summation+=root
        #         res = self.helper(candidates[1:], target, summation)
        #         if res:
        #             print(total)
        #             return True
                
        #     return True
            

    # def combinationSum(self, candidates, target):
    #     total = 0
        # return self.helper(candidates, target, total)
        
sln = Solution()
print(sln.combinationSum([2,3,6,7],7))