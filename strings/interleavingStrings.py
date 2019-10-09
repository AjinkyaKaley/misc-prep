class Solution:
    def interleavingString(self, S1, S2, S3):
        
        if not S1 and not S2 and not S3:
            return True
        if len(S3) == 0:
            return False
        return ( S1 and S1[0] == S3[0] and self.interleavingString(S1[1:],S2,S3[1:])) or (S2 and S2[0]==S3[0] and self.interleavingString(S1,S2[1:],S3[1:]))

sln = Solution()
print(sln.interleavingString("aabcc", "dbbca", "aadbbcbcac"))
