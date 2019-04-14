class Solution:
    def plusOne(self, digits):
        nums = 0
        for i in range(len(digits)):
            nums += digits[i] * pow(10, len(digits)-1-i)
        
        nums+=1
        return [int(i) for i in str(nums)]
        
sln = Solution()
print(sln.plusOne([9,9]))
