class Solution:
    def longestPalindromeSubseq(self, s: 'str') -> 'int':
        
        if len(s) == 0:
            return 0

        if len(s) == 1:
            return 1

        lookup = [[None] * len(s) for i in range(len(s))]

        for idx in range(0,len(s)):
            lookup[idx][idx] = 1

        for length in range(2,len(s)+1):
            for i in range(0, len(s)-length+1):
                j = i + length - 1

                if s[i] == s[j] and length == 2:
                    lookup[i][j] = 2
                elif s[i] == s[j]:
                    lookup[i][j]= lookup[i+1][j-1] + 2
                else:
                    lookup[i][j] = max(lookup[i][j-1], lookup[i+1][j])
        
        print(lookup)
        return lookup[0][len(s)-1]
    
sln = Solution()
print(sln.longestPalindromeSubseq('cbbd'))
