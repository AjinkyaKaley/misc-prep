class Solution:

    def checkPalindrome(self, s):
        return ''.join(reversed(s)) == s

    def nearestPaldindrome(self, n):
        largestLowerPalindrome = int(n)-1
        smallestGreaterPalindrome = int(n) + 1
        
        while not self.checkPalindrome(str(largestLowerPalindrome)):
            largestLowerPalindrome -= 1
        while not self.checkPalindrome(str(smallestGreaterPalindrome)):
            smallestGreaterPalindrome += 1
        
        if abs(int(n) - largestLowerPalindrome) > abs(int(n) - smallestGreaterPalindrome):
            return smallestGreaterPalindrome
        return largestLowerPalindrome
        
sln = Solution()
print(sln.nearestPaldindrome('1234'))
