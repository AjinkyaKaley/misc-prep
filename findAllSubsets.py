import copy;
class Solution:

    def subsets(self, nums, start, subsets, result):

        for i in range(start, len(nums)):
            subsets.append(nums[i])
            self.subsets(nums, i+1, subsets,result)
            del subsets[-1]
        
        result.append(copy.deepcopy(subsets))
        return result

    # def subsets(self, nums, idx, curr):

    #     n = len(nums)
    #     if idx == n:
    #         print(curr)
    #         return
    #     self.subsets(nums, idx+1, curr+[nums[idx]])
    #     self.subsets(nums, idx+1, curr)

sln = Solution()
r = sln.subsets([1,2,3],0,[],[])
print(r)