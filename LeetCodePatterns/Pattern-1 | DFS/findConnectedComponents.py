class Solution:

    def connectedComponentsDFS(self, n, edges):
        from collections import defaultdict
        graph = defaultdict(lambda:[])
        for s,d in edges:
            graph[s].append(d)
            graph[d].append(s)

        visited = set()
        numOfComponents = 0

        def dfs(root):
            visited.add(root)
            for node in graph[root]:
                if node not in visited:
                    dfs(node)
        
        for node in graph.keys():
            if node not in visited:
                dfs(node)
                numOfComponents += 1
        
        return numOfComponents

    def connectedComponentsDFSIter(self, n, edges):
        
        from collections import defaultdict
        graph = defaultdict(lambda: [])
        for s, d in edges:
            graph[s].append(d)
            graph[d].append(s)

        stack = []
        visited = set()
        numOfComponents = 0

        for i in range(n):
            if i not in visited:
                stack.append(i)
                while stack:
                    node = stack.pop()
                    visited.add(node)
                    for n in graph[node]:
                        if n not in visited:
                            stack.append(n)
                numOfComponents += 1
        return numOfComponents
        
sln = Solution()
# print(sln.connectedComponentsDFSIter(
#     n=5, edges=[[0, 1], [1, 2], [2, 3], [3, 4]]))

print(sln.connectedComponentsDFSIter(
    n=5, edges=[[0, 1], [1, 2], [3, 4]]))
