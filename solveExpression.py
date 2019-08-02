from DataStructures.ExpressionTreeNode import ExpressionTreeNode

class Solution:

    def generateExpressionTree(self,postFix):
        stack = []

        def isOperator(ch):
            return ch == '+' or ch == '-' or ch == '*' or ch == '/'

        for c in postFix:
            if not isOperator(c):
                etn = ExpressionTreeNode(c)
                stack.append(etn)
            else:
                etn = ExpressionTreeNode(c)
                operand1 = stack.pop(-1)
                operand2 = None
                if len(stack)>0:
                    operand2 = stack.pop(-1)
                
                etn.left = operand1
                etn.right = operand2
                stack.append(etn)
        root = stack.pop()
        return root
    
    def evaluateExpression(self,root):

        if root.left != None and root.right != None:
            return root.val
        operand1 = self.evaluateExpression(root.left)            
        operand2 = self.evaluateExpression(root.right)
        if root.val == '*':
            return int(operand1) * int(operand2)
        elif root.val == '+':
            return int(operand1) + int(operand2)
        elif root.val == '-':
            return int(operand1) - int(operand2)
        return int(operand1) / int(operand2)
    
sln = Solution()
root = sln.generateExpressionTree("3+5+9*2")
print(sln.evaluateExpression(root))


