class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        def matching(parentheses):
            
            if parentheses == '(':
                return ')'
            
            elif parentheses == '[':
                return ']'
            
            elif parentheses == '{':
                return '}'
            
        OPEN = '([{'
        CLOSED = '])}'
        stack = []
        current_to_match = ''
        for char in s:
            if char in OPEN:
                stack.append(char)
                current_to_match = matching(char)
            
            if char in CLOSED:
                if char == current_to_match:
                    stack.pop()
                    if (stack):
                        current_to_match = matching(stack[-1])
                else:
                    return False
        return not stack

sln = Solution()
testcase = ["((((()))))","(((()())))","(((())()))","(((()))())","(((())))()","((()(())))","((()()()))","((()())())","((()()))()","((())(()))","((())()())","((())())()","((()))(())","((()))()()","(()((())))","(()(()()))","(()(())())","(()(()))()","(()()(()))","(()()()())","(()()())()","(()())(())","(()())()()","(())((()))","(())(()())","(())(())()","(())()(())","(())()()()","()(((())))","()((()()))","()((())())","()((()))()","()(()(()))","()(()()())","()(()())()","()(())(())","()(())()()","()()((()))","()()(()())","()()(())()","()()()(())","()()()()()"]

for parentheses in testcase:
    print(sln.isValid(parentheses))