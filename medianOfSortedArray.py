class Solution:

    def getMaxElement(self, arr, start, end):
        return max(arr[start:end + 1])
    
    def getMinElement(self, arr, start, end):
        return min(arr[start:end+1])

    def helper(self, x, y, low, high):
        low = 0
        high = len(x)
        while low <= high:
            partitionX = (low + high) // 2
            partitionY = ((len(x) + len(y) + 1) // 2) - partitionX

            maxLeftX = float('-inf') if partitionX == 0 else x[partitionX-1]
            minRightX = float('inf') if partitionX == len(x) else x[partitionX]
            maxLeftY = float('-inf') if partitionY == 0 else y[partitionY-1]
            minRightY = float('inf') if partitionY == len(y) else y[partitionY]

            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                if ((len(x) + len(y)) % 2) == 0:
                    return (max(maxLeftX,maxLeftY) + min(minRightX,minRightY)) // 2.0
                return max(maxLeftX, maxLeftY) // 1.0
            elif maxLeftX > minRightY:
                high = partitionX - 1
            else:
                low = partitionX + 1
        return -1

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        x = y = []
        if len(nums1) < len(nums2):
            x = nums1
            y = nums2
        else:
            x = nums2
            y = nums1

        return self.helper(x, y, 0, len(x))
        
sln = Solution()
print(sln.findMedianSortedArrays([1, 3], [2]))
    
