from DataStructures.TreeNode import TreeNode

class Solution:
    def rightSideView(self, root):
        def collect(node, depth):
            if node:
                if depth == len(view):
                    view.append(node.value)
                collect(node.right, depth+1)
                collect(node.left, depth+1)
        view = []
        collect(root, 0)
        return view

def main():
    sln = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.right = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.left.right = TreeNode(7)
    root.left.left = TreeNode(8)
    root.left.right = TreeNode(9)
    print(sln.rightSideView(root))

if __name__ == '__main__':
    main()