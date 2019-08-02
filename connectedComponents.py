class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        self.graph = {node: [] for node in range(n)}
        for e in edges:
            self.graph[e[0]].append(e[1])
            self.graph[e[1]].append(e[0])

        self.visited = {node: False for node in self.graph.keys()}
        count = 0
        for node in self.graph.keys():
            if not self.visited[node]:
                self.dfs(node, self.visited, self.graph)
                count += 1
        return count

    def dfs(self, node, visited, graph):
        visited[node] = True
        for children in graph[node]:
            if not visited[children]:
                self.dfs(children, visited, graph)

sln = Solution()
sln.countComponents(5,[[0, 1], [1, 2], [3, 4]])
