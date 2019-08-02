from collections import defaultdict
class Solution:


    # def canPartitionKSubsets(self, nums, k, iterResult, idx):
    #     lookup = defaultdict(lambda: 0)
    #     def getSubSetSum(nums, k, iterResult, idx, ignoreIdx):
    #         lookup[sum(iterResult)] += 1
            
    #         for i in range(len(nums)):
    #             if ignoreIdx == i:
    #                 continue
    #             iterResult.append(nums[i])
    #             getSubSetSum(nums, k, iterResult, i+1,ignoreIdx)
    #             iterResult.pop()
        
    #     for i in range(len(nums)):
    #         iterResult.append(nums[i])
    #         getSubSetSum(nums, k, iterResult,i+1, 0)
    #         iterResult = []

    #     for key,count in lookup.items():
    #         if count == k:
    #             return True
    #     return False

    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if k == 0 or sum(nums) % 4 != 0:
            return False
        self.used = [False]*len(nums)
        return self.canPartitionKSubsetsUtil(nums, k, 0, sum(nums)//k, 0)

    def canPartitionKSubsetsUtil(self, nums, k, currSum, targetSum, startIdx):
        if k == 0:
            return True

        if currSum == targetSum:
            return self.canPartitionKSubsetsUtil(nums, k-1, 0, targetSum, 0)

        for i in range(startIdx, len(nums)):
            if not self.used[i]:
                self.used[i] = True
                if self.canPartitionKSubsetsUtil(nums, k, currSum+nums[i], targetSum, i+1):
                    return True
                self.used[i] = False
        return False
# Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
# Output: True
# Explanation: It's possible to divide it into 4 subsets(5), (1, 4), (2, 3), (2, 3) with equal sums.
sln = Solution()
d = [4, 3, 2, 3, 5, 2, 1]
print(sln.canPartitionKSubsets(d, 4))
