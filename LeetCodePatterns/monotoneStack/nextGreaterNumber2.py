class Solution:
    def nextGreaterElements(self, nums):

        stack = []
        solution = []
        n = len(nums)
        lookup = {}

        for i in range(2 * len(nums)):
            while stack and nums[stack[-1] % n] <= nums[i % n]:
                idx = stack.pop()
                lookup[nums[idx % n]] = nums[i % n] if (i % n) != (idx % n) else - 1
            stack.append(i)

        for i in nums:
            solution.append(lookup[i])
        return solution

sln = Solution()
print(sln.nextGreaterElements([3, 8, 4, 1, 2]))
        
