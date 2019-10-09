
class Solution:
    def isUnivalTree(self, root):
        def dfs(node):
            if node.left:
                if not dfs(node.left):
                    return False
                if node.left.val != node.val:
                    return False

            if node.right:
                if not dfs(node.right):
                    return False
                if node.right.val != node.val:
                    return False

            return True

        return dfs(root)