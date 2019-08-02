class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        m = len(M)
        n = len(M[0])

        self.union_find = {i: i for i in range(m)}

        def union(x, y):
            parent_x, parent_y = find(x), find(y)
            if parent_x != parent_y:
                self.union_find[parent_x] = parent_y

        def find(x):
            if self.union_find[x] != x:
                self.union_find[x] = find(self.union_find[x])
            return self.union_find[x]

        for i in range(m):
            for j in range(n):
                if M[i][j] == 1:
                    union(i, j)

        parents = set(find(val) for key, val in self.union_find.items())
        return len(parents)


d = [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]

sln = Solution()
sln.findCircleNum(d)