class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        left = 0
        right = len(s)-1
        s=s.strip()
        while left <= right:
            while left < len(s) and not s[left].lower().isalpha():
                left += 1

            while right > 0 and not s[right].lower().isalpha():
                right -= 1
                
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
            
        return True

sln = Solution()
print(sln.isPalindrome(" "))
