from DataStructures.Graph import Graph

class TopologicalSort:

    def topologicalSortUtil(self,i, visited, stack):
        visited[i] = True

        for edge in visited[i]:
            if visited[edge] == False:
                self.topologicalSortUtil(edge, visited, stack)
        stack.insert(0,edge)

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
tpSort = TopologicalSort()
print(tpSort.topologicalSort(6))
