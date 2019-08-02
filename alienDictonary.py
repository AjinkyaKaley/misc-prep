class Node:
    def __init__(self, val):
        self.val = val
        self.color = "white"
        self.neighbors = []

class Solution:
    def alienOrder(self, words):
        letters = set(c for word in words for c in word)
        g = {c:Node(c) for c in letters}
        
        def build_graph():
            for idx in range(len(words)-1):
                first, second = words[idx], words[idx+1]
                k = 0
                while k < min(len(first), len(second)):
                    if first[k] != second[k]:
                        parent, child = first[k], second[k]
                        g[parent].neighbors.append(child)
                        break
                    else:
                        k += 1
        build_graph()
        
        stack = []
        def dfs_visit(v):
            if g[v].color == "black":
                return True
            # Cycle exists
            elif g[v].color == "gray":
                return False
            g[v].color = "gray"
            for neighbor in g[v].neighbors:
                if not dfs_visit(neighbor):
                    return False
            stack.append(v)
            g[v].color = "black"
            return True
        
        for v in g:
            if g[v].color == "white":
                if not dfs_visit(v):
                    return ""
        return "".join(reversed(stack))

sln = Solution()
sln.alienOrder([
    "wrt",
    "wrf",
    "er",
    "ett",
    "rftt"
])