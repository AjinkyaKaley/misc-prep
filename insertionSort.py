class Solution:

    def insertionSort(self, nums):

        for i in range(1, len(nums)):
            j = i-1
            key = nums[i]
            while nums[j] > key and j >= 0:
                nums[j+1] = nums[j]
                j -=1
            nums[j+1] = key
            print(nums)

sln = Solution()
sln.insertionSort([4,3,2,10,12,1,5,6])