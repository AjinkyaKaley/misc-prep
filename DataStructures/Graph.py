from collections import defaultdict

class Graph:

    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices


    def addEdge(self, u, v):
        self.graph[u].append(v)


    def topologicalSortUtil(self, i, visited, stack):
        visited[i] = True

        for edge in self.graph[i]:
            if visited[edge] == False:
                self.topologicalSortUtil(edge, visited, stack)
        stack.insert(0, i)

    def topologicalSort(self, numberOfVertices):
        visited = [False] * numberOfVertices
        stack = list()

        for i in range(numberOfVertices):
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)

        return stack

g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)
print(g.topologicalSort(6))
