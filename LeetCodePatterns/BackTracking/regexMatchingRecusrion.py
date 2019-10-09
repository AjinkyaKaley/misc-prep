class Solution(object):

    
    def isMatch(self, text, pattern):
        if not pattern:
            return not text

        first_match = bool(text) and pattern[0] in {text[0], '.'}

        if len(pattern) >= 2 and pattern[1] == '*':
            return (self.isMatch(text, pattern[2:]) or
                    first_match and self.isMatch(text[1:], pattern))
        else:
            return first_match and self.isMatch(text[1:], pattern[1:])

    def isMatchDP(self, text, pattern):
        dp = [[False for j in range(len(pattern) + 1)] for i in range(len(text) + 1)]
        dp[0][0] = True
        for j in range(1, len(pattern)+1):
            if pattern[j-1] == "*":
                dp[0][j] = dp[0][j - 2]
                
        for i in range(1, len(text)+1):
            for j in range(1, len(pattern)+1):
                if text[i-1] == pattern[j-1] or pattern[j-1] == ".":
                    dp[i][j] = dp[i - 1][j - 1]
                elif pattern[j-1] == "*":
                    dp[i][j] = dp[i][j - 2]
                    if text[i-1] == pattern[j - 2] or pattern[j - 2] == ".":
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
                else:
                    dp[i][j] = False
        return dp[-1][-1]

    

sln = Solution()
print(sln.isMatch('aa', 'a*'))
