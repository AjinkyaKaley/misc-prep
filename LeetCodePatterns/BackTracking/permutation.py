# class Solution:
#     def recPermute(self, result, current, nums):
#         if len(nums) == 2 :
#             result.append(current+[nums[0],nums[1]])
#             result.append(current+[nums[1],nums[0]])
#             return
#         for i in range(len(nums)):
#             self.recPermute(result, current+ [nums[i]], nums[:i]+nums[i+1:])

#     def permute(self, nums):
#         if len(nums) == 0: return [] 
#         if len(nums) == 1 : return [[nums[0]]]

#         result=[]
#         current=[] 
#         self.recPermute(result,current,nums)
#         return result


class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(first=0):
            # if all integers are used up
            if first == n:
                output.append(nums[:])
            for i in range(first, n):
                # place i-th integer first
                # in the current permutation
                nums[first], nums[i] = nums[i], nums[first]
                # use next integers to complete the permutations
                backtrack(first + 1)
                # backtrack
                nums[first], nums[i] = nums[i], nums[first]

        n = len(nums)
        output = []
        backtrack()
        return output


sln = Solution()
print(sln.permute([1,2,3]))
