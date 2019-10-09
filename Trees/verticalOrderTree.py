class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        from collections import defaultdict
        lookup=defaultdict(lambda:defaultdict(list))
        
        def helper(root,x,y):
            if root:
                lookup[x][y].append(root)
                helper(root.left,x-1,y+1)
                helper(root.right,x+1,y+1)
        helper(root,0,0)
        solution=[]
        
        for x in sorted(lookup):
            res = []
            for y in sorted(lookup[x]):
                res.extend(sorted(node.val for node in lookup[x][y]))
            solution.append(res)
        
        return solution

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)

sln = Solution()
sln.verticalTraversal(root)