class Solution:

    def binarySearch(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1

        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                left = mid
                while left > 0 and nums[left-1] == nums[mid]:
                    left -= 1
                right= mid
                while right < len(nums) - 1 and nums[right+1] == nums[mid]:
                    right += 1
                return [left, right]
            elif nums[mid] < target:
                left = mid
            else:
                right = mid

        # Post-processing:
        # End Condition: left + 1 == right
        
        return [-1,-1]

sln = Solution()
input_arry = [5, 7, 7, 8, 8, 10]
sln.binarySearch(input_arry,5)
