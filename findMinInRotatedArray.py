class Solution:

    def findMin(self, nums, low, high):

        if low >= high:
            return nums[low]

        mid = low + (high - low) //2 

        if nums[mid] < nums[high]:
            return self.findMin(nums,low, mid)
        elif nums[mid] > nums[high]:
            return self.findMin(nums,mid+1, high)

sln = Solution()
print(sln.findMin([3,4,5,1,2], 0, 4))