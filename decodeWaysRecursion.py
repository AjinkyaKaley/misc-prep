class Solution:

    def countDecodeWays(self, digits, n):
        if n == 0 or n == 1:
            return 1
        count = 0
        if digits[n-1] > '0':
            count = self.countDecodeWays(digits, n-1)

        if digits[n-2] == '1' or (digits[n-2] == '2' and digits[n-1] < '7'):
            count += self.countDecodeWays(digits, n-2)
        
        return count

sln = Solution()
print(sln.countDecodeWays(list('123'),3))