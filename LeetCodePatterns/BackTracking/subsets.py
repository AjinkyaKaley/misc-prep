import copy
class Solution:

    # Refer fig
    def subsets_2(self, nums):

        self.result = []
        def helper(nums, subsets, startIdx):
            self.result.append(copy.deepcopy(subsets))
            for i in range(startIdx, len(nums)):
                subsets += [nums[i]]
                helper(nums, subsets, i+1)
                subsets.pop()

        helper(nums, [], 0)
        return self.result

sln = Solution()
print(sln.subsets_2([1, 2, 3]))
