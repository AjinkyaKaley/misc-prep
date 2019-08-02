# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # def getMinimumDifference(self, root):
    #     if root.left is None and root.right is None:
    #         return float("inf")
        
    #     leftMin = float("inf")
    #     rightMin = float("inf")
    #     currentLeftMin = float("inf")
    #     currentRightMin = float("inf")

    #     if root.left != None:
    #         leftMin = self.getMinimumDifference(root.left)
    #     if root.right != None:
    #         rightMin = self.getMinimumDifference(root.right)

    #     if root.left != None:
    #         currentLeftMin = abs(root.val - root.left.val)
    #     if root.right != None:
    #         currentRightMin = abs(root.val-root.right.val)
    #     currentLevelMin = min(currentLeftMin,currentRightMin)
    #     subTreeMin = min(leftMin,rightMin)
    #     return min(currentLevelMin,subTreeMin)

    def getMinimumDifferenceInorder(self, root):

        if root.left is None and root.right is None:
            return float("inf")
        leftMin = float("inf")
        rightMin = float("inf")
        if root.left != None:
            leftMin = self.getMinimumDifferenceInorder(root.left)
            leftMin = min(leftMin, abs(root.val-root.left.val))
        if root.right != None:
            rightMin = self.getMinimumDifferenceInorder(root.right)
            rightMin = min(rightMin, abs(root.val-root.right.val))
        return min(leftMin,rightMin)

    def getMinimumDifference(self, root):
        self.ans = 1e9
        self.prev = None
            
        def search(node):
            if node.left: 
                search(node.left)
            if self.prev is not None:
                self.ans = min(self.ans, node.val - self.prev)
            self.prev = node.val
            if node.right: 
                search(node.right)
        search(root)
        return self.ans

sln = Solution()
root = TreeNode(50)
root.left = TreeNode(30)
root.right = TreeNode(75)
root.left.left = TreeNode(20)
root.left.right = TreeNode(40)
root.right.left = TreeNode(60)
root.right.right = TreeNode(80)
print(sln.getMinimumDifference(root))