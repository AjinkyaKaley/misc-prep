class Solution:
    def depthSum(self, nestedList):
        depth = 0
        levelSum = 0

        for item in nestedList:
            if type(item) == list:
                lSum, depth = self.depthSum(item)
                levelSum += lSum
        depth += 1
        
        for item in nestedList:
            if type(item) == int:
                levelSum += depth * item
        
        return (levelSum,depth)

sln = Solution()
sln.depthSum([[1], [[6]]])
