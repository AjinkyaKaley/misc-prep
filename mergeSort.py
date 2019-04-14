class Solution:

    def divide(self, low, high, nums):

        if low == high:
            return [nums[low]]
        
        mid = (low+high)//2
        
        leftList = self.divide(low, mid, nums)
        rightList = self.divide(mid+1, high, nums)
        return self.merge(leftList, rightList)

    def merge(self, left, right):
        result = []
        leftList = []
        rightList = []

        if left[0] <= right[0]:
            leftList = left
            rightList = right
        elif left[0] > right[0]:
            leftList = right
            rightList = left

        l =0
        r =0
        while l < len(leftList) and r < len(rightList):
            if leftList[l] <= rightList[r]:
                result.append(leftList[l])
                l+=1
            elif leftList[l] >= rightList[r]:
                result.append(rightList[r])
                r+=1
        
        if l < len(leftList):
            result.extend(leftList[l:])
        if r < len(rightList):
            result.extend(rightList[r:])
        
        return result

sln = Solution()
test = [9,7,7,8,3,2,1];
print(sln.divide(0, len(test)-1, test))
        