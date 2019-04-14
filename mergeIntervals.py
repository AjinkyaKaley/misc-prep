class Solution:
    idx=1
    def getItem(self, item):
        return item[1]

    def merge(self, intervals):

        sortedIntervals = sorted(intervals,key=self.getItem, reverse=True)
        print(sortedIntervals)
        for i in range(1, len(sortedIntervals)):
            if sortedIntervals[self.idx-1][0] <= sortedIntervals[i][1]:
                while sortedIntervals[self.idx-1][0] <= sortedIntervals[i][1]:
                    sortedIntervals[self.idx-1][0] = min(sortedIntervals[self.idx-1][0],sortedIntervals[i][0])
                    sortedIntervals[self.idx-1][1] = max(sortedIntervals[self.idx-1][1],sortedIntervals[i][1])
                    self.idx-=1
            else:
                sortedIntervals[self.idx] = sortedIntervals[i]
            self.idx +=1
        return sortedIntervals

    def printTest(self, res):
        for i in range(0, self.idx):
            print(res[i])

sln = Solution()
sln.test_case = [[1,5],[2,1],[4,7],[8,10],[15,18]]
t = sln.merge(sln.test_case)
sln.printTest(t)

# [15,18],[8,10],[4,7],[2,1],[1,5]
# [1,3],[2,4],[3,7],[8,10],[15,18]