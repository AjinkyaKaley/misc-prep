class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # -1, 2, 1, -4
        # -4,-1,1,2
        nums.sort()
        i = 0
        tempSum = sum(nums[:3])
        while i < len(nums) -2:
            j = i + 1 
            k = len(nums) -1
            while j < k:
                total = nums[i]+nums[j]+nums[k]
                if total == target:
                    return total
                else:
                    if abs(total-target) < abs(tempSum-target):
                        tempSum = total
                    if total < target:
                        while j+1 < k and nums[j] == nums [j+1]:
                            j+=1
                        j+=1
                    if total > target:
                        while j < k-1  and nums[k] == nums[k-1]:
                            k-=1
                        k-=1
            while nums[i] == nums[i+1] and i < len(nums)-2:
                i+=1
            i+=1
        return tempSum

sln = Solution()
print(sln.threeSumClosest([-1, 2, 1, -4],1))