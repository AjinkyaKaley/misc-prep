class Solution:

    def longestValidParen(self, s):

        stack = [-1]
        result = 0
        for i in range(0, len(s)):
            
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if len(stack) != 0:
                    lengthOfValidParen = i - stack[len(stack) - 1]
                    if lengthOfValidParen > result:
                        result = lengthOfValidParen
                else:
                    stack.append(i)
        return result

sln = Solution()
print(sln.longestValidParen('(()()('))
