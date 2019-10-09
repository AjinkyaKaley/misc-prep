class Solution:
    def triangleNumber(self, nums) -> int:
        self.count = 0
        nums.sort()

        def binarySearch(nums, left, right, target):
            while left <= right:
                mid = (left+right)//2
                if nums[mid] < target:
                    left = mid+1
                else:
                    right = mid-1
            return left

        for i in range(len(nums)-1):
            k = i+2
            for j in range(i+1, len(nums)):
                k = binarySearch(nums, k, len(nums)-1, nums[i]+nums[j])
                self.count += k-j-1
        return self.count

sln = Solution()
sln.triangleNumber([2, 2, 3, 4])