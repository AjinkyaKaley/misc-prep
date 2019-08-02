class Solution:

    def wildCardMatching(self, inputStr, expression):

        if len(inputStr) == 0 and len(expression) == 0:
            return True
        
        if len(expression) > 0 and expression[0] == '*' and len(inputStr) == 0:
            return False
        if (len(inputStr) !=0 and len(expression) !=0 and inputStr[0] == expression[0]) or (len(expression) > 0 and expression[0] == '?'):
            return self.wildCardMatching(inputStr[1:], expression[1:])
        if len(expression) != 0 and expression[0] == '*':
            # very IMPORTANT, first ignore then consider
            # considering first will exhaust the input string and the code willgo in infinite loop
            # View it like how regular expression would work, dont think like NFA DFA, *big mistake*
            # * iterates step by step. ignore it first, as it gaureentes step by step execution
            return self.wildCardMatching(inputStr, expression[1:]) or self.wildCardMatching(inputStr[1:], expression)
        return False 
sln = Solution()
print(sln.wildCardMatching("adceb", "*a*b"))