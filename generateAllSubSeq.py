class Solution:
    
    def generate(self, s):

        if len(s) == 0:
            return

        charInProcess = s[0]
        remainderStr = s[1:]

        for i in range(0,len(remainderStr)):
            subSeq = str(charInProcess + remainderStr[i:])
            print(subSeq)
        
        self.generate(remainderStr)

sln = Solution()
sln.generate('abc')
