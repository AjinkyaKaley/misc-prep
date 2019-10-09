class Solution:

    def validAnagrams(self, s1, s2):
        if len(s1) != len(s2):
            return False
        xor = 0
        for i in range(len(s1)):
            xor = xor ^ ord(s1[i]) ^ ord(s2[i])

sln = Solution()
sln.validAnagrams("anagram", "pagaram")
