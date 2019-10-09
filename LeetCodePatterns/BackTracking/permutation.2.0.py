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
            # answer.append(copy.deepcopy(iterationResult))
            print(''.join(map(str, iterationResult)))
            return

        # visited = set()
        for i in range(0,len(nums)):
            # if nums[i] in visited:
            #     continue

            root = nums[i]
            # visited.add(root)
            newNums = nums[:i] + nums[i+1:]
            iterationResult.append(root)                
            self.dfs(answer,newNums,iterationResult)
            iterationResult.pop()
        # return answer


    def permuteUnique(self, nums):
        self.solution = []
        self.visited = set()

        def perm(nums, curr_perm):
            if len(nums) == 0:
                self.solution += [curr_perm]
                return

            for i in range(len(nums)):
                if nums[i] not in self.visited:
                    self.visited.add(nums[i])
                    perm(nums[:i]+nums[i+1:], curr_perm+[nums[i]])

        perm(nums, [])
        return self.solution

        
sln = Solution()
# sln.permute([1, 2, 3, 4])
sln.permuteUnique([1, 1, 2])

