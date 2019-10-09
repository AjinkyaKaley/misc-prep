class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.val = value

class Solution:
    def preorder(self, root):
        stack = [root]
        solution = []

        while stack:
            node = stack.pop()
            solution.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        print(solution)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(10)
root.right = Node(3)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.left = Node(8)
root.right.left.left.right = Node(9)
sln = Solution()
sln.preorder(root)
