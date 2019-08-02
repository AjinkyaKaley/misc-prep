class Solution:

    def canFinish(self, numCourses, prerequisites):
        
        class Node:
            def __init__(self, value):
                self.value = value
                self.edges = []
                self.color = 'white'

        graph = {vertex: Node(vertex) for vertex in range(numCourses)}
        
        for course,preq in prerequisites:
            graph[course].edges.append(preq)

        def dfs(node):
            if graph[node].color == 'grey':
                return False
            graph[node].color = 'grey'
            for e in graph[node].edges:
                if not dfs(e):
                    return False
            graph[node].color = 'black'
            return True

        for course in range(numCourses):
            if graph[course].color == 'white':
                if not dfs(course):
                    return False
        return True

sln = Solution()
print(sln.canFinish(6, [[5,2],[5,0],[4,0],[4,1],[2,3],[3,1],[0,3]]))
