
class Interval:

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __lt__(self, other):
        return self.start < other.start


class Solution:
    idx=1
    def getItem(self, item):
        return item[0]

    def merge(self, intervals):

        sortedIntervals = sorted(intervals,key=self.getItem, reverse=True)
        print(sortedIntervals)
        for i in range(1, len(sortedIntervals)):
            if sortedIntervals[self.idx-1][1] <= sortedIntervals[i][0]:
                while self.idx >0 and sortedIntervals[self.idx-1][0] <= sortedIntervals[i][1]:
                    sortedIntervals[self.idx-1][0] = min(sortedIntervals[self.idx-1][0],sortedIntervals[i][0])
                    sortedIntervals[self.idx-1][1] = max(sortedIntervals[self.idx-1][1],sortedIntervals[i][1])
                    self.idx-=1
            else:
                sortedIntervals[self.idx] = sortedIntervals[i]
            self.idx +=1
        return sortedIntervals

    def mergeWithoutSpace(self, intervals):
        sortedIntervals = sorted(intervals,key=self.getItemAsce)
        idx = len(sortedIntervals)
        for i in range(1,idx-1):
            interval = sortedIntervals[i]
            if sortedIntervals[i-1][1] >= interval[0]:
                sortedIntervals[i-1][0] = min(sortedIntervals[i-1][0],sortedIntervals[i][0])
                sortedIntervals[i-1][1] = max(sortedIntervals[i-1][1],sortedIntervals[i][1])
                idx-=1
                del sortedIntervals[i]
        
        return sortedIntervals

    def merge_(self, intervals):
        _intervals = [Interval(start, end) for start, end in intervals]
        sortedIntervals = sorted(_intervals)
        solution = [sortedIntervals[0]]
        n = len(sortedIntervals)
        for i in range(1, n):
            if solution[-1].end >= sortedIntervals[i].start:
                solution[-1].start = min(solution[-1].start,
                                         sortedIntervals[i].start)
                solution[-1].end = max(solution[-1].end,
                                       sortedIntervals[i].end)
            else:
                solution.append(sortedIntervals[i])

        return [[inter.start, inter.end] for inter in solution]


    def printTest(self, res):
        for i in range(0, self.idx):
            print(res[i])
    
    def getItemAsce(self, item):
        return item[0]

    def mergeIntervalsWithStack(self, intervals): 
        sortedIntervals = sorted(intervals, key=self.getItemAsce)
        lookup = []
        lookup.append(sortedIntervals[0])

        for i in range(1,len(sortedIntervals)):
            interval = sortedIntervals[i]
            if lookup[len(lookup)-1][1] >= interval[0]:
                temp = lookup[len(lookup)-1]
                temp[0] = min(temp[0],interval[0])
                temp[1] = max(temp[1],interval[1])
            else:
                lookup.append(interval)

        print(lookup)




sln = Solution()
sln.test_case = [[1, 3], [2, 6], [8, 10], [15, 18]]
t = sln.merge_(sln.test_case)
sln.printTest(t)

# [15,18],[8,10],[4,7],[2,1],[1,5]
# [1,3],[2,4],[3,7],[8,10],[15,18]
