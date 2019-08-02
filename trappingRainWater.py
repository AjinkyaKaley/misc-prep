class Solution:
    def trappingRainWater(self, nums):
        
        ans = 0
        for i in range(len(nums)):
            max_left = 0
            max_right = 0
            for j in range(i, -1, -1):
                max_left = max(max_left, nums[j])
            for k in range(i, len(nums)):
                max_right = max(max_right, nums[k])
            ans += min(max_left, max_right) - nums[i]
        return ans
sln = Solution()
print(sln.trappingRainWater([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
