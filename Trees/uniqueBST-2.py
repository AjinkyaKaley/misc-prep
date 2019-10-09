class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def generateTrees(self, n: int):
        result = []
        root = None
        return self.helper([i for i in range(1,n+1)],result, root,0)


    def helper(self, n, result, root, start):
        
        if n[start] > root or start > len(n):
            return None
        
        for i in range(start,len(n)):
            r = result[n[i]]
            leftVal = self.helper(n, result, r, i+1)
            rightVal = self.helper(n, result, r, i+2)

