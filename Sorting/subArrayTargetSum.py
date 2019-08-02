class Solution:

    def subArrayTarget(self, nums, target, idx, lengthTillNow):
        if target == 0:
            print(lengthTillNow)
        if target < 0:
            return
        for i in range(idx, len(nums)):
            self.subArrayTarget(nums, target - nums[i], i + 1, lengthTillNow + 1)

sln = Solution()
sln.subArrayTarget([1,2,3,4],6,0,0)