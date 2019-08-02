class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) ==1:
            return 0
        
        low = 0
        high = len(nums)-1
        while low<=high:
            mid = (low+high)//2
            if ((mid==0 or nums[mid-1] <= nums[mid]) and (mid==len(nums)-1 or nums[mid+1]<= nums[mid])):
                return mid
            if nums[mid-1] > nums[mid]:
                high = mid -1
            elif nums[mid+1] > nums[mid]:
                low = mid + 1

sln = Solution()
sln.findPeakElement([1,2])