class Solution(object):
    def isMatch(self, inputStr, expression):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [[False for j in range(len(expression)+1)]
              for i in range(len(inputStr)+1)]
        dp[0][0] = True
        for j in range(1, len(expression)+1):
            if expression[j-1] != '*':
                break
            dp[0][j] = True

        for i in range(1, len(inputStr)+1):
            for j in range(1, len(expression)+1):
                if (inputStr[i-1] == expression[j-1]) or (expression[j-1] == '?'):
                    dp[i][j] = dp[i-1][j-1]
                elif expression[j-1] == '*':
                    dp[i][j] = dp[i][j-1] or dp[i-1][j]
                else:
                    dp[i][j] = False

        return dp[-1][-1]

sln = Solution()
print(sln.isMatch("aa","*"))
