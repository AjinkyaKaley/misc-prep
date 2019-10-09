class Solution(object):
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        def DFS(nestedList, depth,solution):
            # temp_sum = 0
            for member in nestedList:
                if type(member) == int:
                    solution.append(member)
                else:
                    DFS(member, depth+1, solution)
            return solution
        return DFS(nestedList, 1, [])
sln = Solution()
print(sln.depthSum([[1, 1], 2, [1, 1]]))
