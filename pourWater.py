class Solution(object):
    def __init__(self):
        self.leftStack = []
        self.rightStack = []

	# update self.leftStack starting from idx
    def pushLeft(self, heights, idx):
        for i in range(idx, 0, -1):
            if heights[i - 1] < heights[i]:
                self.leftStack.append(i - 1)
            elif heights[i - 1] > heights[i]:
                break  # stops quickly when there is a bump.

    # update self.rightStack starting from idx
    def pushRight(self, heights, idx):
        for i in range(idx, len(heights) - 1):
            if heights[i + 1] < heights[i]:
                self.rightStack.append(i + 1)
            elif heights[i + 1] > heights[i]:
                break

	# update self.leftStack when drops at DropIdx
    def leftDropOn(self, dropIdx, heights):
        if dropIdx > 0:
            if heights[dropIdx - 1] < heights[dropIdx]:
                # no need to update others on the left side (e.g. [1,3,2,2,2*,4])
                self.leftStack.append(dropIdx - 1)
            elif heights[dropIdx - 1] == heights[dropIdx]:
                # update when a dip is filled (e.g. [1,3,2*,3,3,4]).
                self.pushLeft(heights, dropIdx)

	# update self.rightStack when drops at DropIdx
    def rightDropOn(self, dropIdx, heights):
        if dropIdx < len(heights) - 1:
            if heights[dropIdx + 1] < heights[dropIdx]:
                self.rightStack.append(dropIdx + 1)
            elif heights[dropIdx + 1] == heights[dropIdx]:
                self.pushRight(heights, dropIdx)

    def pourWater(self, heights, V, K):
        """
        :type heights: List[int]
        :type V: int
        :type K: int
        :rtype: List[int]
        """
        if K < 0 or K >= len(heights):
            return heights

        # initialization
        self.pushLeft(heights, K)
        self.pushRight(heights, K)

        for i in range(V):
            if len(self.leftStack):
			    # pop the location that water drops to
                dropIdx = self.leftStack.pop()
                heights[dropIdx] += 1

		# don't lose this position where it is still a decreasing point
                if heights[dropIdx] < heights[dropIdx + 1]:
                    self.leftStack.append(dropIdx)
                # maintain the invariant
                self.leftDropOn(dropIdx, heights)
            elif len(self.rightStack):
                dropIdx = self.rightStack.pop()
                heights[dropIdx] += 1
                if heights[dropIdx] < heights[dropIdx - 1]:
                    self.rightStack.append(dropIdx)
                self.rightDropOn(dropIdx, heights)
            else:
                heights[K] += 1
                self.leftDropOn(K, heights)
                self.rightDropOn(K, heights)
        return heights

sln = Solution()
sln.pourWater([2, 1, 1, 2, 1, 2, 2], V=4, K=3)
