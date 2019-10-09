import copy

class Solution:

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        self.answer = []
        return self.dfs(self.answer,nums,[])

    def dfs(self, answer, nums, iterationResult):
        
        if len(nums) == 0:
            answer.append(copy.deepcopy(iterationResult))
            return

        visited = set()
        for i in range(0,len(nums)):
            if nums[i] in visited:
                continue

            root = nums[i]
            visited.add(root)
            newNums = nums[:i] + nums[i+1:]
            iterationResult.append(root)                
            self.dfs(answer,newNums,iterationResult)
            iterationResult.pop()
        return answer

sln = Solution()
print(sln.permute([1,1,2,2]))