
class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val
        
class Solution:
    def levelOrderTraversal(self, root):
        from collections import deque
        queue = deque([root])
        result = []
        while queue:
            l_result = []
            lenq = len(queue)
            for i in range(lenq):
                temp = queue.pop()
                if temp.left:
                    queue.appendleft(temp.left)
                if temp.right:
                    queue.appendleft(temp.right)
                l_result.append(temp.val)
            result.append(l_result)
        return result


root = TreeNode(7)
root.left = TreeNode(8)
root.right = TreeNode(9)
root.left.left = TreeNode(10)
root.left.right = TreeNode(11)
root.right.left = TreeNode(12)
sln = Solution()
print(sln.levelOrderTraversal(root))