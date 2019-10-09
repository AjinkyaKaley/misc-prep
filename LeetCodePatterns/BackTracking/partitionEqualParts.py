class Solution:
    def canPartitionKSubsets(self, nums, k: int):
        equal_sum = sum(nums)//k
        self.solution = []
        visited = set()
        nums.sort()
        def helper(startIdx, nums,k,curr_sub_seq, curr_sum):
            if k == 0:
                return True
            if curr_sum == equal_sum:
                self.solution += [curr_sub_seq]
                return helper(0,nums,k-1,[],0)
            
            for i in range(startIdx,len(nums)):
                if i not in visited and curr_sum + nums[i] <= equal_sum:
                    visited.add(i)
                    if helper(i+1,nums,k, curr_sub_seq+[nums[i]],curr_sum+nums[i]):
                        return True
                    visited.discard(i)
            return False
        return helper(0,nums,k,[],0)
            
sln = Solution()
sln.canPartitionKSubsets([10, 10, 10, 7, 7, 7, 7, 7, 7, 6, 6, 6],
                         3)
