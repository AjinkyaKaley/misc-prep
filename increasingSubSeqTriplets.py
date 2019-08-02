class Solution:

    def findTriplets(self, nums):
        smaller = [0 for i in range(len(nums))]
        greater = [0 for i in range(len(nums))]
        minIdx = 0
        maxIdx = len(nums)-1
        smaller[0] = -1
        greater[maxIdx] = -1

        for i in range(1, len(nums)):
            if nums[i] <= nums[minIdx]:
                minIdx = i
                smaller[i] = -1
            else:
                smaller[i] = minIdx

        for i in range(len(nums)-2,-1,-1):
            if nums[i] >= nums[maxIdx]:
                maxIdx = i
                greater[i] = -1
            else:
                greater[i] = maxIdx

        print(smaller)
        print(greater)

        for i in range(0, len(nums)):
            if smaller[i] != -1 and greater[i] != -1:
                print(str(nums[smaller[i]]) + "," + str(nums[i]) + "," + str(nums[greater[i]]))

    def increasingTriplet(self, nums):
        first = second = float('inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False

sln = Solution()
sln.findTriplets([100, 10, 101, 11, 102, 12])
