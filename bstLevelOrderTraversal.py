# Definition for a binary tree node.
import copy
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: 'TreeNode') -> 'List[List[int]]':
        q = []
        q.append(root)
        result = []
        while q:
            t=copy.deepcopy(q)
            result.append([x.val for x in q])
            q=[]
            while t:
                r = t.pop(0)
                if r.left:
                    q.append(r.left)
                if r.right:
                    q.append(r.right)
        return result
        
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)
root.right.right = TreeNode(7)
root.right.left = TreeNode(15)

sln = Solution()   
res = sln.levelOrder(root)

for i in res:
    print(i)