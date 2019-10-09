
class Solution:

    def depthSum(self,nestedList):
        totalSum = 0
        depth = 1
        def helper(nestedList, depth, currSum):
            for i in range(len(nestedList)):
                if type(nestedList[i]) == int:
                    currSum += depth*nestedList[i]
                else:
                    currSum = helper(nestedList[i], depth + 1, currSum)
            return currSum

        return helper(nestedList, depth, 0)
sln = Solution()
# print(sln.depthSum([[1, 1], 2, [1, 1]]))
print(sln.depthSum([1, [4, [6]]]))