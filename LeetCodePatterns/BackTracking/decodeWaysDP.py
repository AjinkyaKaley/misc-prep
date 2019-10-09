class Solution:

    def helper(self, digits, k, memo):

        if k == 0 or k == 1:
            return 1
        
        if digits[k-1] == '0':
            return 0
        
        if memo[k] != None:
            print("Returning : " + str(memo[k]) )
            return memo[k]
        
        result = self.helper(digits, k-1, memo)
        if  digits[k-2] == '1' or (digits[k-2] == '2' and digits[k-1] < '7'):
            result += self.helper(digits, k-2, memo)
        
        memo[k] = result
        return result

sln = Solution()
memo = [None] * 6
print(sln.helper("10", 5,memo))