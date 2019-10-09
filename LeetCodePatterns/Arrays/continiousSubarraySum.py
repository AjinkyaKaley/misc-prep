class Solution:

    # This technique will not work for input [0],k=0 or [0,1,0], k = 0
    # use other technique
    def checkSubarraySumBetter(self, nums, k):
        if len(nums) < 2:
            return False

        aux = [0] * (len(nums) + 1)
        for i in range(1, len(aux)):
            aux[i] = aux[i - 1] + nums[i - 1]
            
        for left in range(len(nums)):
            for right in range(left + 1, len(nums) + 1):
                _s = aux[right] - aux[left]
                if ( _s == k) or (k != 0 and (_s % k == 0)):
                    return True
        return False

    # This technique accumulates left sum till i and value of i itself
    # while processing, i.e looking for left boundary it subtracts the whole of left and add the value i from nums
    def checkSubarraySumAlterApproach(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        aux = [0] * (len(nums))
        for i in range(1, len(aux)):
            aux[i] = aux[i - 1] + nums[i]

        for left in range(len(nums)-1):
            for right in range(left + 1, len(nums)):
                _s = aux[right] - aux[left] + nums[left]
                if (_s == k) or (k != 0 and (_s % k == 0)):
                    return True
        return False

    def checkSubarraySumBruteForce(self, nums, k):
        
        for start in range(len(nums)):
            for end in range(start + 1, len(nums) + 1):
                _s = sum(nums[start:end])
                if _s == k or (k!=0 and _s % k == 0):
                    return True

        return False
sln = Solution()
# print(sln.checkSubarraySumBetter([23, 2, 4, 6, 7], k=6))
print(sln.checkSubarraySumBetter([0,1,0], k=0))
# 
