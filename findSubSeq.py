class Solution:

    def subSequence(self, lookupStr, s):
        if lookupStr == "":
            return True
        
        charInProcess = lookupStr[0]
        remainderStr = lookupStr[1:]
        print( "lookupStr : " + lookupStr + " main str : " + s)
        for j in range(0, len(s)):
            if s[j] == charInProcess:
                return self.subSequence(remainderStr, s[j+1:])
        return False

# AXY -> ADXCPY

sln = Solution()
print(sln.subSequence('gksrek', 'geeksforgeeks'))