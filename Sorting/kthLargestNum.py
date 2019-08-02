class Solution:

    def partition(self, nums, low, high):
        pivot = nums[high]
        i = low - 1
        j = 0
        for j in range(low, high):
            if nums[j] <= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1], nums[high] = nums[high], nums[i + 1]
        return i + 1
        
    def kthLargest(self, nums, low, high,k):
        if low < high:
            partitionIdx = self.partition(nums, low, high)
            if len(nums) - k == partitionIdx:
                print(nums[partitionIdx])
                return
            self.kthLargest(nums, low, partitionIdx - 1,k)
            self.kthLargest(nums, partitionIdx + 1, high,k)
        
sln = Solution()
nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
sln.kthLargest(nums, 0, len(nums)-1, 4)
