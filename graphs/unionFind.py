class Solution:
    def validTree(self, n: int, edges):

        graph = {i: i for i in range(n)}

        def find(x):
            if graph[x] != x:
                graph[x] = find(graph[x])
            return graph[x]

        def union(x, y):
            _x = find(x)
            _y = find(y)
            if _x == _y:
                return False
            graph[_x] = _y
            return True

        for edge in edges:
            if not union(edge[0], edge[1]):
                return False
        return len(edges) == n - 1
        
sln = Solution()
sln.validTree(5, [[0, 1], [0, 4], [1, 4], [2, 3]])
