class Solution:
    def dominantIndex(self, nums):
        highest=-1
        secondHighest = -1
        highestIdx = -1
        
        for i in range(0,len(nums)):
            if nums[i] > highest:
                secondHighest = highest                 
                highest = nums[i]
                highestIdx = i
            elif nums[i] >= secondHighest:
                secondHighest = nums[i]
        return highestIdx if highest >= 2*secondHighest else -1

sln = Solution()
print(sln.dominantIndex([0,0,3,2]))