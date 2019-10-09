class Solution:

    def dfsIter(self, matrix):

        n = len(matrix)
        visited = set()
        stack = []
        friendCirle = 0
        for i in range(n):
            if i not in visited:
                stack.append(i)
                while stack:
                    f = stack.pop()
                    visited.add(f)
                    for j in range(n):
                        if matrix[f][j] == 1 and j not in visited:
                            stack.append(j)

                friendCirle += 1

        return friendCirle

    def dfsRecur(self, matrix):
        visited = set()
        friendCircle = 0
        n = len(matrix)

        def helper(i):
            if i not in visited:
                visited.add(i)
                for c in range(len(matrix)):
                    if matrix[i][c] == 1 and c not in visited:
                        helper(c)
        
        for i in range(n):
            if i not in visited:
                helper(i)
                friendCircle += 1
        return friendCircle
sln = Solution()
# print(sln.dfs([[1, 1, 0],
#                [1, 1, 1],
#                [0, 1, 1]]))

print(sln.dfsRecur([[1, 1, 0],
                    [1, 1, 1],
                    [0, 1, 1]]))
