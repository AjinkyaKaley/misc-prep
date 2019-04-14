class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        startPtr=0
        endPtr=1

        while endPtr<len(s) and s[endPtr] == s[endPtr+1]:
            endPtr+=1
        s = s[:endPtr+1] + s[endPtr] + s[endPtr:]
        k-=1
        

sln=Solution()
sln.characterReplacement('AABABBA',1) 
