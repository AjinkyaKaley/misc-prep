class Solution:

    # def calculate(self, s):
    #     if not s:
    #         return "0"
    #     stack, num, sign = [], 0, "+"
    #     for i in range(len(s)):
    #         if s[i].isdigit():
    #             num = num*10+ord(s[i])-ord("0")
    #         if (not s[i].isdigit() and not s[i].isspace()) or i == len(s)-1:
    #             if sign == "-":
    #                 stack.append(-num)
    #             elif sign == "+":
    #                 stack.append(num)
    #             elif sign == "*":
    #                 stack.append(stack.pop()*num)
    #             else:
    #                 tmp = stack.pop()
    #                 if tmp//num < 0 and tmp%num != 0:
    #                     stack.append(tmp//num+1)
    #                 else:
    #                     stack.append(tmp//num)
    #             sign = s[i]
    #             num = 0
    #     return sum(stack)

    def precedenceOp(self, op1):
        if op1 == '+' or op1 == '-':
            return 1
        if op1 == '*' or op1 == '/':
            return 2

    def applyOp(self, val1, val2, op):
        if op == '+':
            return val1 + val2
        if op == '-':
            return val1 - val2
        if op == '*':
            return val1 * val2
        else:
            return val1 // val2
            
    def calculate(self, s):
        values = []
        operator = []
        if not s:
            return "0"
        num = 0
        i = 0
        while i < len(s):
            if s[i] == ' ':
                i += 1
                continue
            if s[i].isdigit():
                while i < len(s) and s[i].isdigit():
                    num = num * 10 + ord(s[i])-ord("0")
                    i += 1
                values.append(num)
            else:
                while operator and self.precedenceOp(operator[-1]) > self.precedenceOp(s[i]):
                    val2 = values.pop()
                    val1 = values.pop()
                    op = operator.pop()
                    values.append(self.applyOp(val1, val2, op))
                operator.append(s[i])
                num = 0
                i += 1
        while operator:
            val2 = values.pop()
            val1 = values.pop()
            op = operator.pop()
            values.append(self.applyOp(val1, val2, op))
            
        return values[-1]
sln = Solution()
print(sln.calculate(" 3/2 "))
