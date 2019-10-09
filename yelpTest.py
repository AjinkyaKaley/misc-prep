class Node:
    def __init__(self, b):
        self.name = b
        self.children = dict()

class Solution:

    def radius(self, root, target, curr, solution):
        for b, d in root.children.items():
            if curr + d <= target:
                solution.append(b.name)
                self.radius(b,target,curr+d,solution)
        return solution

root = Node('A')
nodeB = Node('B')
nodeC = Node('C')
nodeD = Node('D')
nodeE = Node('E')
nodeF = Node('F')

root.children[nodeB] = 1
root.children[nodeC] = 1

nodeB.children[nodeD] = 1
nodeB.children[nodeE] = 2

nodeC.children[nodeF] = 5

sln = Solution();
print(sln.radius(root,0,0,[]))
