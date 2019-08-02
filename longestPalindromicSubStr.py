class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        if len(s) == 0:
            return ''

        if len(s) == 1:
            return s
        
        if len(s) == 2 and s[0] != s[1]:
            return s[0]

        lookup = [[None] * len(s) for i in range(len(s))]
        maxLength = 0
        start = 0
        for idx in range(0,len(s)):
            lookup[idx][idx] = True

            if idx < len(s)-1 and s[idx] == s[idx+1]:
                lookup[idx][idx+1] = True
                maxLength = 2
                start = idx

        for l in range(3, len(s)+1):
            for i in range(0,len(s)-l+1):
                j = i + l -1
                # print("length = " + str(l) + " " + "i = " + str(i) + " j " + str(j))
                if s[i] == s[j] and lookup[i+1][j-1]:
                    lookup[i][j] = True
                    if l > maxLength:
                        maxLength = l
                        start = i
        if maxLength == 0:
            return s[start: start+maxLength+1]
        return s[start: start+maxLength]
        
    def longestPalindromeDP(self, s):
        """
        :type s: str
        :rtype: str
        """
        dp = [[ 1 if i==j else 0 for j in range(len(s))]for i in range(len(s))]
        startIdx = float("inf")

        for l in range(2, len(s)+1):
            for i in range(0, len(s) - l + 1):
                j = i + l - 1
                if l == 2 and s[i] == s[j]:
                    dp[i][j] = 2
                    startIdx = min(i, startIdx)
                elif s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                    startIdx = min(i, startIdx)
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i+1][j])

        maxLen = dp[0][len(s)-1]

        return s[startIdx:startIdx+maxLen]

sln = Solution()
print(sln.longestPalindrome('abcda'))
