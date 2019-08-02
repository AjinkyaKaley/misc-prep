class Solution:
    def reverseWords(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s) - 1
        self.reverse(s, i, j)
        start = 0
        for i in range(len(s)):
            if s[i] == ' ':
                self.reverse(s, start, i - 1)
                start = i + 1
            elif i == len(s) - 1:
                self.reverse(s, start, i)
                
    def reverse(self, s,i,j):
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
            
            
sln = Solution()
sln.reverseWords(["t", "h", "e", " ", "s", "k", "y",
                  " ", "i", "s", " ", "b", "l", "u", "e"])
