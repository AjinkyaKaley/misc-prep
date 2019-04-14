# class Solution:

#     def gen_parens(self, curr_string, combinations, remaining, curr_open):
        
#         if remaining == 0 and curr_open == 0:
#             # print(curr_string)
#             combinations.append(curr_string)
#             print('FINAL :' + curr_string)
#             print('------------------------')
#             return

#         if remaining > 0:
#             print('RETURN AT OPEN '+'current: ' + curr_string + ' remaining: ' + str(remaining) + ' curr_open: ' + str(curr_open))
#             self.gen_parens(curr_string+'(', combinations, remaining-1, curr_open+1)
#         if remaining <= curr_open or curr_open == 1:
#             print('RETURN AT CLOSE '+'current: ' + curr_string + ' remaining: ' + str(remaining) + ' curr_open: ' + str(curr_open))
#             self.gen_parens(curr_string+')', combinations, remaining, curr_open-1)

#         print('RETURN AT END '+'current: ' + curr_string + ' remaining: ' + str(remaining) + ' curr_open: ' + str(curr_open))
    
#     def generateParenthesis(self, n: 'int') -> 'List[str]':
#         if n == 0:
#             return []
        
#         rv = []
#         self.gen_parens('', rv, n, 0)
#         print(rv)
#         return rv


# sln = Solution()
# sln.generateParenthesis(3)



class Solution:
    def gen_parens(self, curr_string, combinations, remaining, curr_open):
        if remaining == 0 and curr_open == 0:
            combinations.append(curr_string)
            return      
        if remaining > 0:
            self.gen_parens(curr_string+'(', combinations, remaining-1, curr_open+1)
        if curr_open > 0:
            self.gen_parens(curr_string+')', combinations, remaining, curr_open-1)
    
    def generateParenthesis(self, n: 'int') -> 'List[str]':
        if n == 0:
            return []
        
        rv = []
        self.gen_parens('', rv, n, 0)
        print(rv)
        return rv

sln = Solution()
sln.generateParenthesis(3)