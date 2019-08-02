class Solution:
    def productExceptSelf(self, nums):
        leftProduct = [1] * len(nums)
        rightProduct = [1] * len(nums)
        result = [0] * len(nums)
        for i in range(1, len(nums)):
            leftProduct[i] = leftProduct[i-1] * nums[i-1]
        
        for j in range(len(nums)-2, -1, -1):
            rightProduct[j] = rightProduct[j+1] * nums[j+1]

        for idx in range(0,len(nums)):
            result[idx] = leftProduct[idx] * rightProduct[idx]
        
        return result
    
    # slower apparently
    def productExceptItselfBetter(self, nums):
        leftProduct = [1] * len(nums)
        n = len(nums)
        result = [0] * len(nums)
        for i in range(1, len(nums)):
            leftProduct[i] = leftProduct[i-1] * nums[i-1]
        
        result[n-1] = leftProduct[n-1]
        leftProduct[n-1] = nums[n-1]

        for i in range(len(nums)-2,-1,-1):
            result[i] = leftProduct[i+1] * leftProduct[i]
            leftProduct[i] = nums[i] * leftProduct[i+1] 
        return result
    #copied
    def productExceptFaster(self, nums):
            
            ans = [1 for _ in range(len(nums))]
            
            left_mul = 1
            for index in range(len(nums)):
                ans[index] *= left_mul
                left_mul *= nums[index]
            
            right_mul = 1
            for index in range(len(nums) - 1, -1, -1):
                ans[index] *= right_mul
                right_mul *= nums[index]
            
            return ans
sln = Solution()
print(sln.productExceptFaster([1, 2, 3, 4]))
