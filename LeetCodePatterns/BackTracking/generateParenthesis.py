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