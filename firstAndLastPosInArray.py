class Solution:

    def binarySearch(self, low, high, nums, target):

        if low > high:
            return [-1,-1]
        mid = (high+low)//2
        if nums[mid] == target:
            left = mid
            right = mid
            while left > 0 and nums[left-1] == nums[mid]:
                left-=1
            while right < len(nums)-1 and nums[right+1] == nums[mid]:
                right+=1

            return [left, right]
        
        if target < nums[mid]:
            return self.binarySearch(low, mid-1, nums, target)
        elif target > nums[mid]:
            return self.binarySearch(mid+1, high, nums, target)

sln = Solution()
print(sln.binarySearch(0,2,[2,2],3))